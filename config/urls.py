from django.contrib import admin
from django.urls import include, path

from users.views import CookSignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", CookSignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("kitchen.urls", namespace="kitchen")),
]
