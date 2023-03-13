from django import forms
from postings.models import Posting


class PostingForm(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    company = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    location = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={"class": "input"}),
    )
    website = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"class": "input"}),
    )
    logo = forms.ImageField(
        required=False,
        widget=forms.FileInput(
            attrs={
                # "class": "block rounded-md mt-1 w-full shadow-sm border border-light-bg2 focus:border-primary-bg focus:ring focus:ring-primary-bg focus:ring-opacity-50 file:bg-primary-bg",
                "class": "input p-2 cursor-pointer hover:file:text-primary-hover file:bg-primary-bg file:border-none file:text-primary-fg file:p-2 file:rounded-md"
            }
        ),
    )
    description = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "input",
                "rows": 5,
            }
        ),
    )

    class Meta:
        model = Posting
        fields = [
            "title",
            "company",
            "location",
            "email",
            "website",
            "tags",
            "logo",
            "description",
        ]
