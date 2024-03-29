# Generated by Django 5.0.1 on 2024-01-04 12:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Davlat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Karobka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='Avto_photo/')),
            ],
        ),
        migrations.CreateModel(
            name='Rang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Yeyishi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rusum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='model_rusumi', to='avto.model')),
            ],
        ),
        migrations.CreateModel(
            name='Viloyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('davlat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='viloyatlar', to='avto.davlat')),
            ],
        ),
        migrations.CreateModel(
            name='Shahar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shaharlar', to='avto.viloyat')),
            ],
        ),
        migrations.CreateModel(
            name='Avto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yili', models.CharField(max_length=4, verbose_name='Yili')),
                ('kraska_holati', models.CharField(max_length=50, verbose_name='Kraska Holati')),
                ('narhi', models.IntegerField(verbose_name='Narhi')),
                ('data', models.DateField(auto_now_add=True)),
                ('yana', models.TextField(verbose_name="qo'shimcha")),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_user', to='User.user', verbose_name='User')),
                ('karobka', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_karobkasi', to='avto.karobka', verbose_name='Karobka')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_modeli', to='avto.model', verbose_name='Modeli')),
                ('photo', models.ManyToManyField(to='avto.photo', verbose_name='Rasm')),
                ('rang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_rangi', to='avto.rang', verbose_name='Rangi')),
                ('rusum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_rusumi', to='avto.rusum', verbose_name='Rusumi')),
                ('shahar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_shahari', to='avto.shahar', verbose_name='Shahar')),
                ('yeyishi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avto_yeyishi', to='avto.yeyishi', verbose_name='Yeyishi')),
            ],
        ),
    ]
