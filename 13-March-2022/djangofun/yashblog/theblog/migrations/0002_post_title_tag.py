# Generated by Django 4.0.3 on 2022-03-13 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='CHILL!!!!', max_length=255),
        ),
    ]