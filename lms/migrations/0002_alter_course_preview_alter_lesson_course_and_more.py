# Generated by Django 5.1.3 on 2024-12-01 19:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="lms/pictures", verbose_name="Превью"
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="lessons",
                to="lms.course",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="preview",
            field=models.ImageField(
                blank=True, null=True, upload_to="lms/pictures", verbose_name="Превью"
            ),
        ),
    ]