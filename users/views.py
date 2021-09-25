""" Users views """

# Django REST Framework
from rest_framework import permissions, mixins, status,viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
# Model
from users.models import User
# Serializer
from users.serializers import UserModelSerializer, UserLoginSerializer
# Permissions
from rest_framework.permissions import (AllowAny, IsAuthenticated)
"""
class UserListView(generics.ListCreateAPIView):
    "User view list and create"
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
"""
class UserViewSet(mixins.CreateModelMixin,
                mixins.ListModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                viewsets.GenericViewSet):
    """User view set.
    Handle sign up and, login account.
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    def get_permissions(self):
        """ Assign permissions based on action """
        if self.action in ['login', 'list']:
            permissions = [AllowAny]
        elif self.action in ['retrieve', 'update', 'create']:
            permissions = [IsAuthenticated]
        else:
            permissions = [IsAuthenticated]
        return [p() for p in permissions]

    @action(detail = False, methods=['post'])
    def login(self, request):
        """ User sign in """
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user' : UserModelSerializer(user).data,
            'access_token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)