# Generated by Django 4.2.7 on 2023-12-15 13:15

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0014_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]