# Generated by Django 5.0.2 on 2024-02-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Nepa_application', '0011_alter_topic_province_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='topic',
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ManyToManyField(related_name='topics', to='Nepa_application.category'),
        ),
    ]