from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from postings.views import SignUpView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("postings.urls", namespace="postings")),
    path("__reload__/", include("django_browser_reload.urls")),
    path("signup", SignUpView.as_view(), name="sign-up"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
