from django.urls import path
from postings import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = "postings"

urlpatterns = [
    path("", views.PostingListView.as_view(), name="postings-list"),
    path("postings/<pk>/", views.PostingDetailView.as_view(), name="postings-detail"),
    path(
        "postings/<pk>/update",
        views.PostingUpdateView.as_view(),
        name="postings-update",
    ),
    path(
        "postings/<pk>/delete",
        views.PostingDeleteView.as_view(),
        name="postings-delete",
    ),
    path("postings/create", views.PostingCreateView.as_view(), name="postings-create"),
    path("signup", views.SignUpView.as_view(), name="sign-up"),
    path("login", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(), name="logout"),
]
