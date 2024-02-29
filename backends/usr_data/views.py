from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from .models import usr_data
from .serializers import usr_data_serializer
# Create your views here.

class usr_data_view(viewsets.ModelViewSet):
    queryset = usr_data.objects.all().order_by('device_id')
    serializer_class = usr_data_serializer

    def create(self, request, *args, **kwargs):
        device_id = request.data.get('device_id')
        existing_record = usr_data.objects.filter(device_id=device_id).first()
        if existing_record:
            serializer = self.get_serializer(existing_record, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK if existing_record else status.HTTP_201_CREATED, headers=headers)