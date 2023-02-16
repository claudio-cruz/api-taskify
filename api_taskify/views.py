from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view()
def root_route(request, format=None):
    return Response({
        'message': 'Taskify API',
    })
