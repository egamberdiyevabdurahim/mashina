from django.db import models

from User.models import User


class Davlat(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Viloyat(models.Model):
    name = models.CharField(max_length=50)
    davlat = models.ForeignKey(Davlat, on_delete=models.CASCADE, related_name='viloyatlar')

    def __str__(self):
        return f'{self.davlat}/{self.name}'


class Shahar(models.Model):
    name = models.CharField(max_length=50)
    viloyat = models.ForeignKey(Viloyat, on_delete=models.CASCADE, related_name='shaharlar')

    def __str__(self):
        return f'{self.viloyat}/{self.name}'


class Model(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rusum(models.Model):
    name = models.CharField(max_length=30)
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='model_rusumi')

    def __str__(self):
        return f'{self.model}/{self.name}'


class Karobka(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Rang(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Yeyishi(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(upload_to='Avto_photo/')


class Avto(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='avto_modeli', verbose_name='Modeli')
    rusum = models.ForeignKey(Rusum, on_delete=models.CASCADE, related_name='avto_rusumi', verbose_name='Rusumi')
    yili = models.CharField(max_length=4, verbose_name='Yili')
    photo = models.ManyToManyField(Photo , verbose_name='Rasm')
    yeyishi = models.ForeignKey(Yeyishi, on_delete=models.CASCADE, related_name='avto_yeyishi', verbose_name='Yeyishi')
    karobka = models.ForeignKey(Karobka, on_delete=models.CASCADE, related_name='avto_karobkasi', verbose_name='Karobka')
    rang = models.ForeignKey(Rang, on_delete=models.CASCADE, related_name='avto_rangi', verbose_name='Rangi')
    kraska_holati = models.CharField(max_length=50, verbose_name='Kraska Holati')
    shahar = models.ForeignKey(Shahar, on_delete=models.CASCADE, related_name='avto_shahari', verbose_name='Shahar')
    narhi = models.IntegerField(verbose_name='Narhi')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='avto_user', verbose_name='User')
    data = models.DateField(auto_now_add=True)
    yana = models.TextField(verbose_name=f'qo\'shimcha')

    def __str__(self):
        return f'{self.rusum}/{self.narhi}/{self.shahar}'
