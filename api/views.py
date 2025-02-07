from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets


from .serializers import GroupSerializer, UserSerializer


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
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# @api_view(["POST"])
# @permission_classes([permissions.AllowAny])
# def user_authenticate(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     # user = User.objects.filter(username=username).first()

#     user = User.objects.get(username=username)
#     token, created = Token.objects.get_or_create(user=user)
#     print(token.key)

#     if user and user.check_password(password):
#         return Response({"success": "User authenticated"})
#     return Response({"error": "Invalid credentials"}, status=400)
