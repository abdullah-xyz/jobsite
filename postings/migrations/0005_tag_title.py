# Generated by Django 4.1.7 on 2023-03-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("postings", "0004_tag_alter_posting_logo_posting_tags"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="title",
            field=models.CharField(default="NA", max_length=50),
            preserve_default=False,
        ),
    ]
