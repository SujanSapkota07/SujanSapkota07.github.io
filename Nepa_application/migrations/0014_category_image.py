# Generated by Django 5.0.2 on 2024-02-15 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nepa_application', '0013_category_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default='', upload_to='category_images'),
        ),
    ]
