from django.views import generic
from postings.models import Posting
from django.urls import reverse_lazy


class PostingListView(generic.ListView):
    model = Posting
    template_name = "postings/posting-list.html"
    context_object_name = "postings"


class PostingDetailView(generic.DetailView):
    model = Posting
    template_name = "postings/posting_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["Delete"] = "code to delete"
    #     print(context["object"].id)
    #     print(context)
    #     return context


class PostingCreateView(generic.CreateView):
    model = Posting
    template_name = "postings/posting_create.html"
    fields = "__all__"
    success_url = reverse_lazy("postings:postings-list")


class PostingUpdateView(generic.UpdateView):
    model = Posting
    template_name = "postings/posting_create.html"
    fields = "__all__"
    success_url = reverse_lazy("postings:postings-list")


class PostingDeleteView(generic.DeleteView):
    model = Posting
    template_name = "postings/posting_create.html"

    success_url = reverse_lazy("postings:postings-list")
