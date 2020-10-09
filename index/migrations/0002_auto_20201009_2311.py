# Generated by Django 3.1.2 on 2020-10-09 23:11

from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=11)),
                ('photo', models.ImageField(blank=True, upload_to=index.models.object_directory_path('original_size'))),
                ('photo600', models.ImageField(blank=True, upload_to=index.models.object_directory_path('600x600'))),
                ('photo450', models.ImageField(blank=True, upload_to=index.models.object_directory_path('450x450'))),
                ('photo300', models.ImageField(blank=True, upload_to=index.models.object_directory_path('300x300'))),
                ('photo200', models.ImageField(blank=True, upload_to=index.models.object_directory_path('200x200'))),
                ('photo150', models.ImageField(blank=True, upload_to=index.models.object_directory_path('150x150'))),
                ('photo100', models.ImageField(blank=True, upload_to=index.models.object_directory_path('100x100'))),
                ('photo75', models.ImageField(blank=True, upload_to=index.models.object_directory_path('75x75'))),
                ('photo37', models.ImageField(blank=True, upload_to=index.models.object_directory_path('37x37'))),
                ('photo18', models.ImageField(blank=True, upload_to=index.models.object_directory_path('18x18'))),
            ],
            options={
                'db_table': 'profile_photos',
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='index.photo'),
        ),
    ]
