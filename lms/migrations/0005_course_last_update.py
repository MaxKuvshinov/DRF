# Generated by Django 5.1.3 on 2024-12-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0004_subscription"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="last_update",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
