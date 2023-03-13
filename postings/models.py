from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class Tag(models.Model):
    title = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Posting(models.Model):
    title = models.CharField(max_length=200, help_text=_("title of job"))
    company = models.CharField(
        max_length=200, help_text=_("name of company posting job")
    )
    location = models.CharField(max_length=300, help_text=_("location of job"))
    email = models.EmailField(max_length=200, help_text=_("contact for company"))
    website = models.CharField(max_length=60, help_text=_("website of the company"))
    logo = models.ImageField(
        upload_to="logo/", blank=True, null=True, help_text=_("logo of the company")
    )
    description = models.TextField(help_text=_("description of job"))
    tags = models.ManyToManyField(Tag)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
