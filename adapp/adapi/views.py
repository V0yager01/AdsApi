from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from user.models import User

from .serializers import AdSerializer, UserCreateSerializer
from .models import Ad


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']
    


class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            User.objects.create_user(**serializer.data)
            return Response("User created", status=status.HTTP_201_CREATED)
