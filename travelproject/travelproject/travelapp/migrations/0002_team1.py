# Generated by Django 4.1.7 on 2023-03-23 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Team_name', models.CharField(max_length=250)),
                ('Team_img', models.ImageField(upload_to='pics')),
                ('Team_desc', models.TextField()),
            ],
        ),
    ]