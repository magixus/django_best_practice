
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from learn.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse


def index(request):
    return HttpResponse("app is working thank you")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]