# Generated by Django 3.2.7 on 2021-09-24 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0014_auto_20210924_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tproducts',
            name='country',
            field=models.CharField(choices=[('eng', '영국'), ('spa', '스페인'), ('net', '네덜란드'), ('ran', '프랑스'), ('ita', '이탈리아'), ('swi', '스위스'), ('cze', '체코'), ('tur', '터키'), ('thi', '태국'), ('tai', '대만')], max_length=3, verbose_name='여행국가'),
        ),
    ]
