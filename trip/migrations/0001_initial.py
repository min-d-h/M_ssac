# Generated by Django 3.2.6 on 2021-09-20 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tproducts',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('tname', models.CharField(max_length=50, unique=True, verbose_name='여행상품')),
                ('start_date', models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')),
                ('s_trip1', models.DateField(verbose_name='출발날짜')),
                ('s_trip2', models.DateField(verbose_name='도착날짜')),
                ('country', models.CharField(choices=[('eng', '영국'), ('spa', '스페인'), ('net', '네덜란드'), ('ran', '프랑스'), ('ita', '이탈리아'), ('swi', '스위스'), ('cze', '체코'), ('tur', '터키'), ('hon', '홍콩'), ('thi', '태국')], max_length=3, verbose_name='여행국가')),
                ('count', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], max_length=1, verbose_name='인원수')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50, verbose_name='아이디\x1d')),
                ('username', models.CharField(max_length=50, verbose_name='사용자명')),
                ('password', models.CharField(max_length=50, verbose_name='비밀번호')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='이메일')),
                ('text', models.TextField(null=True, verbose_name='소개')),
                ('registered', models.DateTimeField(auto_now_add=True, verbose_name='등록')),
                ('gender', models.CharField(choices=[('M', '남성(Man)'), ('W', '여성(Woman)')], max_length=1, verbose_name='성별')),
            ],
        ),
    ]