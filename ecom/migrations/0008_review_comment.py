# Generated by Django 3.0.5 on 2021-11-12 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='comment',
            field=models.TextField(default='nice', max_length=250),
        ),
    ]
