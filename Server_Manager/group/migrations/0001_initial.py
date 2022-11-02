# Generated by Django 4.1.2 on 2022-11-02 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupName', models.CharField(max_length=200)),
                ('groupDescription', models.TextField(null=True)),
                ('groupCredentials', models.CharField(max_length=200)),
            ],
        ),
    ]