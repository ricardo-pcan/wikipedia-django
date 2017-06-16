# -*- coding: utf-8 -*-
from wiki_django.api.v1.routers import router
from wiki_django.core.api import mixins
from wiki_django.core.api.viewsets import GenericViewSet
from subprocess import call
from django.http import HttpResponse

class EventViewSet(
        mixins.ListModelMixin,
        GenericViewSet):

    def list(self, request, *args, **kwargs):
        """
        Return events list.
        ---
        response_serializer: serializers.EventSerializer
        parameters:
            - name: fromdate
              description: initial date. Format YYYY-MM-DD
              paramType: query
              type: string
            - name: place
              description: filter by place id
              paramType: query
              type: integer
            - name: todate
              description: end date. Format YYYY-MM-DD
              paramType: query
              type: string
        responseMessages:
            - code: 200
              message: OK
            - code: 403
              message: FORBIDDEN
            - code: 500
              message: INTERNAL SERVER ERROR
        consumes:
            - application/json
        produces:
            - application/json
        """

        call(["mw-zip", "-c", ":es", "-o", "test.zip", "Éter etílico"])
        call(["mw-render", "-c", "test.zip", "-o", "test.pdf", "-w", "rl"])

        return HttpResponse("Here's the text of the Web page.")


router.register(
    r'events',
    EventViewSet,
    base_name="events"
)
