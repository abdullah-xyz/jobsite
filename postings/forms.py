from django.forms import ModelForm
from postings.models import Posting


class PostingForm(ModelForm):
    class Meta:
        model = Posting
        fields = [
            "title",
            "company",
            "location",
            "email",
            "website",
            "logo",
            "description",
        ]
