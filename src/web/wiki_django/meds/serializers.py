# -*- coding: utf-8 -*-
from redsep_offline.core.api.serializers import ModelSerializer
from redsep_offline.meds.models import Med, Theme

from rest_framework import serializers


class ThemeSerializer(ModelSerializer):
    block = serializers.SerializerMethodField()
    grade = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()

    class Meta:
        model = Theme
        fields = (
            'id',
            'name',
            'block',
            'grade',
            'level',
            'subject',
            'is_oficial'
        )

    def get_block(self, instance):
        return instance.block.name

    def get_grade(self, instance):
        return instance.block.subject.grade.name

    def get_level(self, instance):
        return instance.block.subject.grade.level.name

    def get_subject(self, instance):
        return instance.block.subject.name


class MedSerializer(ModelSerializer):
    themes = ThemeSerializer(many=True)

    class Meta:
        model = Med
        fields = [
            'id',
            'title',
            'description',
            'thumbnail',
            'donated_by',
            'reference_url',
            'donor_website',
            'type_class',
            'themes',
            'created_date'
        ]
