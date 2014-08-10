from gtxapi.models import Task
from gtxapi.serializers import TaskSerializer, UserSerializer
from rest_framework import generics, permissions, viewsets, renderers
from django.contrib.auth.models import User
from gtxapi.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view, link
from rest_framework.response import Response
from rest_framework.reverse import reverse



@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })


class TaskViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    @link(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)

    def pre_save(self, obj):
        obj.owner = self.request.user



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
