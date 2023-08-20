from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.utils.decorators import method_decorator
from accounts.models import UserAccount
from django.contrib import auth


@method_decorator(csrf_protect, name="dispatch")
class CheckIfAuthenticated(APIView):
    def get(self, resquest, format=True):
        isAuth = UserAccount.is_authenticated

        return Response({"isAuth": isAuth})


@method_decorator(csrf_protect, name="dispatch")
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        data = self.request.data
        password = data["password"]
        username = data["username"]
        # verify data
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            return Response(
                {
                    "details": "cant login",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            auth.login(request=request, user=user)
            return Response(
                UserAccount.objects.get(username=username, password=password)
            )


class LogoutView(APIView):
    def get(self, request, format=None):
        auth.logout()


@method_decorator(csrf_protect, name="dispatch")
class RegisterView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def post(self, request, format=None):
        name1 = request.data["name1"]
        name2 = request.data["name2"]
        password1 = request.data["password1"]
        password2 = request.data["password2"]

        if password1 != password2:
            return Response(
                "passwords does not match",
                status=status.HTTP_400_BAD_REQUEST,
            )
        if not name1 or not name2:
            return Response("first name and or last name required")


# to be able to get csrf_cookie in this route
@method_decorator(ensure_csrf_cookie, name="dispatch")
class CSRFToken(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request, format=None):
        return Response("CSRF cookie set", status=status.HTTP_200_OK)
