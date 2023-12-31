from django.urls import path
from .views import Sign_Up, Log_in, Info, Log_out, PublicInfo

urlpatterns = [
    path("info/", Info.as_view(), name="info"),
    path("signup/", Sign_Up.as_view(), name='signup'),
    path("login/", Log_in.as_view(), name="login"),
    path("logout/", Log_out.as_view(), name='logout'),
    path("public/<int:user_id>/",PublicInfo.as_view(), name="public_info")
]