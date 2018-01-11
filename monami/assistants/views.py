from assistants.models import Assistant
from django.contrib.auth.models import User
from assistants.models import Appointment
from assistants.serializers import AssistantSerializer
from assistants.serializers import UserSerializer
from assistants.serializers import AppointmentSerializer
from django.http import Http404
# import django_filters.rest_framework
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from django.views.decorators.csrf import ensure_csrf_cookie
# import django_filters.rest_framework

class AssistantList(generics.ListCreateAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('last_name', 'first_name', 'household', 'companion', 'driver')


class AssistantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assistant.objects.all()
    serializer_class = AssistantSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('username')

class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)


class AppointmentList(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
# , assistant= self.request.assistant
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('date', 'owner', 'assistant')


class AppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


@api_view(['GET'])
@ensure_csrf_cookie


# @authentication_classes((SessionAuthentication, BasicAuthentication))
# @permission_classes((IsAuthenticated,))
@ensure_csrf_cookie
def api_root(request, format=None):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        # 'assistants': reverse('assistant-list', request=request, format=format),
        # 'appointments': reverse('appointment-list', request=request, format=format),
        # 'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        # 'auth': unicode(request.auth),  # None
    })

#
