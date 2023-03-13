from django.views import generic
from postings.models import Posting
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from users.forms import UsersUserCreationForm
from postings.forms import PostingForm


class SignUpView(generic.CreateView):
    form_class = UsersUserCreationForm
    template_name = "postings/signup.html"
    success_url = reverse_lazy("postings:postings-list")


class PostingListView(generic.ListView):
    model = Posting
    template_name = "postings/posting-list.html"
    context_object_name = "postings"
    paginate_by = 6


class PostingDetailView(generic.DetailView):
    model = Posting
    template_name = "postings/posting_detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["Delete"] = "code to delete"
    #     print(context["object"].id)
    #     print(context)
    #     return context


class PostingCreateView(LoginRequiredMixin, generic.CreateView):
    # model = Posting
    form_class = PostingForm
    template_name = "postings/posting_create.html"
    # fields = "__all__"
    success_url = reverse_lazy("postings:postings-list")

    def form_valid(self, form):
        posting = form.save(commit=False)
        posting.created_by = self.request.user
        posting.save()
        return super().form_valid(form)


class PostingUpdateView(LoginRequiredMixin, generic.UpdateView):
    # model = Posting
    def get_queryset(self):
        user = self.request.user
        return Posting.objects.filter(created_by=user)

    form_class = PostingForm
    template_name = "postings/posting_create.html"
    # fields = "__all__"
    success_url = reverse_lazy("postings:postings-list")


class PostingDeleteView(LoginRequiredMixin, generic.DeleteView):
    # model = Posting
    template_name = "postings/posting_create.html"

    success_url = reverse_lazy("postings:postings-list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[""] = ""
        print(context)
        return context

    def get_queryset(self):
        user = self.request.user
        return Posting.objects.filter(created_by=user)
