# Generated by Django 5.0.2 on 2024-02-14 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0007_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phonenumber', models.IntegerField()),
                ('company', models.CharField(max_length=90)),
                ('address1', models.TextField()),
                ('address2', models.TextField()),
                ('address3', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
