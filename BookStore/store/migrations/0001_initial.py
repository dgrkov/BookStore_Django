# Generated by Django 5.0.3 on 2024-05-27 16:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('state_province', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('num_pages', models.IntegerField()),
                ('cover', models.CharField(choices=[('H', 'Hardcover'), ('P', 'Paperback'), ('E', 'E-book')], max_length=1)),
                ('genre', models.CharField(choices=[('R', 'Romance'), ('D', 'Drama'), ('T', 'Thriller'), ('F', 'Fantasy'), ('S', 'Sci-Fi'), ('H', 'Horror'), ('M', 'Mystery')], max_length=1)),
                ('cover_picture', models.ImageField(upload_to='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.author')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.publisher')),
            ],
        ),
    ]
