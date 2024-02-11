# views.py

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

class TestViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {'message': 'This is a test response from the backend!'}
        return Response(data, status=status.HTTP_200_OK)
