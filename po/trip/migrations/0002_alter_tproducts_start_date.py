# Generated by Django 3.2.6 on 2021-09-20 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tproducts',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='등록날짜'),
        ),
    ]
