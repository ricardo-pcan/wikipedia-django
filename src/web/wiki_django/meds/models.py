# -*- coding: utf-8 -*-
import os
from hashlib import md5

from django.core.urlresolvers import reverse
from django.db import models

from redsep_offline.core.db.models import CatalogueMixin, TimeStampedMixin

from slugify import slugify


def get_thumbnail_path(instance, filename):
    """
    Get the upload path to the image.
    """
    return '{0}/{1}{2}'.format(
        "meds",
        md5(filename.encode('utf-8')).hexdigest(),
        os.path.splitext(filename)[-1]
    )


def get_resource_path(instance, filename):
    """
    Get the upload path to the resources
    """
    ext = filename.split('.')[-1]
    resource_digest = md5(filename.encode('utf-8')).hexdigest()
    resource_name = slugify(
        " ".join(
            [instance.med.title.encode('utf-8'), resource_digest[:8]]
        ),
        separator='_',
        save_order=True
    )
    return "{0}/{1}.{2}".format(
        "resources",
        resource_name,
        ext
    )


class BaseCurricularAlignmentModel(TimeStampedMixin):
    name = models.CharField(
        max_length=600
    )
    position = models.PositiveIntegerField(
        default=0
    )
    is_active = models.BooleanField(
        default=True
    )
    is_oficial = models.BooleanField(
        default=True
    )
    slug = models.SlugField(
        max_length=500,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['position']


class Level(BaseCurricularAlignmentModel):
    """
    Defines model for school level in curricular alignment
    """

    class Meta:
        verbose_name = u'Nivel'
        verbose_name_plural = u'Niveles'


class Grade(BaseCurricularAlignmentModel):
    """
    Defines model for school grade in curricular alignment
    """
    level = models.ForeignKey(
        Level,
        related_name='grades'
    )

    class Meta:
        verbose_name = u'Grado'
        verbose_name_plural = u'Grados'


class Subject(BaseCurricularAlignmentModel):
    """
    Defines model for subject in curricular alignment
    """
    grade = models.ForeignKey(
        Grade,
        related_name='subjects'
    )

    class Meta:
        verbose_name = u'Materia'
        verbose_name_plural = u'Materias'


class Block(BaseCurricularAlignmentModel):
    """
    Defines model for block in curricular alignment
    """
    subject = models.ForeignKey(
        Subject,
        related_name='blocks'
    )

    class Meta:
        verbose_name = u'Bloque'
        verbose_name_plural = u'Bloques'


class Theme(BaseCurricularAlignmentModel):
    """
    Defines model for theme in curricular alignment
    """
    block = models.ForeignKey(
        Block,
        related_name='themes'
    )

    class Meta:
        verbose_name = u'Tema'
        verbose_name_plural = u'Temas'


class MedType(CatalogueMixin):
    """
    Defines model for Type of MED
    """
    description = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )

    slug = models.SlugField(
        max_length=600,
    )

    class Meta(CatalogueMixin.Meta):
        verbose_name = 'Tipo de recurso digital'
        verbose_name_plural = 'Tipos de recursos digitales'


class MedSubType(CatalogueMixin):
    """
    Defines model for Sub-Type of MED
    """
    description = models.CharField(
        max_length=300,
        blank=True,
        null=True
    )
    med_type = models.ForeignKey(
        MedType,
        related_name='subtypes',
        null=True, blank=True
    )

    slug = models.SlugField(
        max_length=600,
    )

    class Meta(CatalogueMixin.Meta):
        verbose_name = 'Subtipo de recurso digital'
        verbose_name_plural = 'Subtipos de recursos digitales'


class Med(TimeStampedMixin):
    """
    Defines model for MED
    """
    title = models.CharField(
        max_length=600
    )
    description = models.TextField(
        verbose_name=u'descripción',
        blank=True,
        null=True
    )
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        upload_to=get_thumbnail_path,
        max_length=400
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=u'is active'
    )
    original_id = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name=u'ID original'
    )

    # Fields for donated resources
    donated_by = models.CharField(
        max_length=256,
        default="",
        verbose_name=u'donated by'
    )
    reference_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name=u'reference url'
    )
    donor_website = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name=u'donor website'
    )

    # Relations
    type_class = models.ForeignKey(
        MedType,
        related_name='meds'
    )
    subtype = models.ForeignKey(
        MedSubType,
        blank=True, null=True
    )
    themes = models.ManyToManyField(Theme)

    @property
    def categorizations_list(self):
        """
        Returns a string of categorization maps, related with the resource.
        """
        themes = self.themes.all()
        categorizations = ""

        for theme in themes:
            categorizations += '{0} > {1} > {2} > {3} > {4}\n'.format(
                theme.block.subject.grade.level.name.encode('utf-8'),
                theme.block.subject.grade.name.encode('utf-8'),
                theme.block.subject.name.encode('utf-8'),
                theme.block.name.encode('utf-8'),
                theme.name.encode('utf-8'),
            )

        return categorizations

    def get_absolute_url(self):
        return reverse(
            'api:v1:meds-detail',
            kwargs={'pk': self.id}
        )

    def __unicode__(self):
        return self.title

    class Meta(CatalogueMixin.Meta):
        verbose_name = 'Recurso digital'
        verbose_name_plural = 'Recursos digitales'


class Resource(TimeStampedMixin):
    """
    Defines model for Resource of MED
    """
    attached_file = models.FileField(
        upload_to=get_resource_path,
        verbose_name="file",
        max_length=400
    )
    attached_file_size = models.PositiveIntegerField(
        default=0,
        verbose_name="file size"
    )
    format_file = models.CharField(
        max_length=45,
        blank=True,
        null=True
    )

    # When the file is compressed as a zip, the directory to the path where
    # the file is uncompressed should be stored
    #
    uncompressed_directory = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name='uncompressed directory'
    )
    #
    # Some resources are flash format. Some browsers don't have support, so
    # the user should state when a flash resource is uploaded
    #
    is_flash = models.BooleanField(
        default=False,
        verbose_name='is flash'
    )

    # Relations
    med = models.ForeignKey(
        Med,
        related_name='resources'
    )

    def __unicode__(self):
        return u'{} - {}'.format(
            self.med.title.encode('utf-8').decode('utf-8'),
            self.format_file
        )

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
