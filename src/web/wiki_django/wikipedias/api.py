# -*- coding: utf-8 -*-
from wiki_django.api.v1.routers import router
from rest_framework.decorators import list_route
from wiki_django.core.api.viewsets import GenericViewSet
from subprocess import call
import random
from django.http import HttpResponse

class WikipediaViewSet(
        GenericViewSet):

    @list_route(methods=['GET'])
    def get_pdf(self, request, *args, **kwargs):
        """
        Return events list.
        ---
        response_serializer: serializers.EventSerializer
        parameters:
            - name: fromdate
              description: initial date. Format YYYY-MM-DD
        print query_params
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


        query_params = self.request.query_params
        title = query_params.get('title', None)
        hash = random.getrandbits(16)
        hash = str(hash)

        call(['mw-zip', '-c', ':es', '-o', '/tmp/'+hash+'.zip', title])
        call(['mw-render', '-c', '/tmp/'+hash+'.zip', '-o', '/tmp/'+hash+'.pdf', '-w', 'rl'])

        with open('/tmp/'+hash+'.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename='+hash+'.pdf'
            return response


router.register(
    r'wikipedias',
    WikipediaViewSet,
    base_name="wikipedias"
)
