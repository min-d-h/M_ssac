# Generated by Django 3.2.6 on 2021-09-20 18:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0010_alter_tproducts_tname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tproducts',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, unique=True, verbose_name='등록날짜'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tproducts',
            name='tname',
            field=models.CharField(max_length=50, verbose_name='여행상품'),
        ),
    ]
