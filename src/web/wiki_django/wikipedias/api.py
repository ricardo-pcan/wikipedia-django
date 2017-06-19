# -*- coding: utf-8 -*-
from wiki_django.api.v1.routers import router
from rest_framework.decorators import list_route
from wiki_django.core.api.viewsets import GenericViewSet
from rest_framework import status
from subprocess import check_call, CalledProcessError
import random
from django.http import HttpResponse

class WikipediaViewSet(
        GenericViewSet):

    @list_route(methods=['GET'])
    def get_pdf(self, request, *args, **kwargs):
        """
        Return wikipedia pdf by title.
        ---
        parameters:
            - name: title
              description: filter by title id
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

        try:
            check_call(['mw-zip', '-c', ':es', '-o', '/tmp/'+hash+'.zip', title])
            check_call(['mw-render', '-c', '/tmp/'+hash+'.zip', '-o', '/tmp/'+hash+'.pdf', '-w', 'rl'])
        except CalledProcessError as error:
            response = HttpResponse(
                error.strerror,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
            return response

        with open('/tmp/'+hash+'.pdf', 'rb') as pdf:
            response = HttpResponse(pdf.read(),content_type='application/pdf')
            response['Content-Disposition'] = 'filename='+hash+'.pdf'
            response['status'] = status.HTTP_200_OK
            return response


router.register(
    r'wikipedias',
    WikipediaViewSet,
    base_name="wikipedias"
)
