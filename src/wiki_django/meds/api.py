# -*- coding: utf-8 -*-
from redsep_offline.api.v1.routers import router
from redsep_offline.core.api import mixins
from redsep_offline.core.api.viewsets import GenericViewSet
from redsep_offline.meds.models import Med
from redsep_offline.meds.serializers import MedSerializer


class MedViewSet(
        GenericViewSet,
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin):

    serializer_class = MedSerializer
    list_serializer_class = MedSerializer
    retrieve_serializer_class = MedSerializer

    queryset = Med.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        """
        Return a med list.
        ---
        response_serializer: MedSerializer

        responseMessages:
            - code: 200
              message: OK
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(MedViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Return a specific med.
        ---
        response_serializer: MedSerializer

        responseMessages:
            - code: 200
              message: OK
            - code: 403
              message: FORBIDDEN
            - code: 404
              message: NOT FOUND
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """
        return super(MedViewSet, self).retrieve(request, args, kwargs)


router.register(
    r"meds",
    MedViewSet,
    base_name="meds"
)
