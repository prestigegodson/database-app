from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloController(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return list of apiview functions"""

        api_list = [
            'Returns http methods (GET,POST,PUT,DELETE,PATCH)',
            'Hello world',
        ]

        return Response({'message': 'Successful', 'data': api_list})

    def post(self, request):
        """Create a new post request"""

        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

        name = serializer.validated_data.get('name')
        message = f'name is {name}'

        return Response({'message': message})


class HelloViewSet(viewsets.ViewSet):
    """View set example"""

    serializer_class = serializers.HelloSerializer

    def list(self, request, format=None):
        """Get list of viewset"""

        a_viewset = [
            'ada',
            'obi'
        ]

        return Response({'message': 'successful', 'data': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'error': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            name = serializer.validated_data.get('name');
            message = f'name = {name}'

            return Response({'message': 'successful', 'data': message})

    def retrieve(self, request, pk=None):
        """Get name by id"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Update name"""
        return Response({'method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """Partially update name"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Delete name by id"""
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """This class handles user profile request"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')


class UserLoginApiView(ObtainAuthToken):
    """
    Create a login api that returns auth token to caller
    """

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES