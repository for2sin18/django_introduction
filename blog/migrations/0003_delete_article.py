# Generated by Django 3.2.7 on 2022-04-12 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
    ]