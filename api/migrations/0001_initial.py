# Generated by Django 3.0.1 on 2021-01-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('details', models.CharField(max_length=200)),
                ('detect', models.ImageField(blank=True, upload_to='detects/')),
            ],
        ),
    ]
