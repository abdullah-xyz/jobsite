from django.contrib import admin
from postings.models import Posting, Tag

# Register your models here.
admin.site.register(Posting)
admin.site.register(Tag)
