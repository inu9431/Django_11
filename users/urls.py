from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path("", views.Users.as_view()), # api/v1/users
    path("myinfo", views.MyInfo.as_view()), # api/v1/users/myinfo
    path("getToken", obtain_auth_token), # api/v1/users/myinfo
    path("login/", views.Login.as_view()), # django session login
    path("logout/", views.Logout.as_view()), # django session login
    path("login/jwt", views.JWTLogin.as_view()),
    path("login/jwt/info", views.UserDetailView.as_view()),
    path("login/simplejwt/", TokenObtainPairView.as_view()),
    path("login/simplejwt/refesh", TokenRefreshView.as_view()),
    path("login/simplejwt/verify", TokenVerifyView.as_view()),
]