from django.urls import path
from postings import views

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
]
