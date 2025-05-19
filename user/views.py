from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from user.serializers import UserSerializer

@api_view(["GET"])
def user_root(request, format=None):
    return Response({
        "register": reverse("user:register", request=request, format=format),
        "me": reverse("user:user-manage", request=request, format=format),
        "token": reverse("user:token_obtain_pair", request=request, format=format),
        "token_refresh": reverse("user:token_refresh", request=request, format=format),
    })


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
