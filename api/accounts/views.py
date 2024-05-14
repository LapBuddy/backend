from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions, status, viewsets
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ChangePasswordSerializer,
    RegisterSerializer,
    UserSerializer,
    UserProfileSerializer,
)

from django.middleware.csrf import get_token
from rest_framework.decorators import api_view, permission_classes


# Admin viewset to view/ update/ delete/ users
class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )


# Login API
# Example POST: {"username":"name","password":"12345"}
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


# Logout API
# Needs the authorization token in header like so:
# Authorization: Token <insert_token_here>
class LogoutAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        request._auth.delete()
        logout(request)
        return Response(
            {"message": "User logged out successfully"}, status=status.HTTP_200_OK
        )


# Get/update User profile API
class UserAPI(generics.RetrieveAPIView, generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.request.user
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = User.objects.filter(username=user.username)
            user.update(
                first_name=serializer.data.get("first_name"),
                last_name=serializer.data.get("last_name"),
                email=serializer.data.get("email"),
            )
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Profile updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """

    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                "status": "success",
                "code": status.HTTP_200_OK,
                "message": "Password updated successfully",
                "data": [],
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([AllowAny])
def csrf(request):
    "Returns CSRF token"
    return Response({"csrfToken": get_token(request)}, status=status.HTTP_200_OK)
