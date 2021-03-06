# Generated by Django 4.0.4 on 2022-05-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=10)),
                ('no_of_pages', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
