# Generated by Django 3.2.3 on 2022-08-20 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('LIBRARIAN', 'LIBRARIAN'), ('MEMBER', 'MEMBER'), ('Admin', 'Admin')], max_length=20),
        ),
    ]
