from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe


class User(AbstractUser):
    is_director = models.BooleanField(default=False)
    is_children = models.BooleanField(default=False)


class Director(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Пользователь',primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Наименование детского дома')
    address = models.CharField(max_length=400, verbose_name='Адрес')
    phonenumber = models.CharField(max_length=11, verbose_name='Номер телефона')

    class Meta:
        verbose_name = f'Представитель детского дома'
        verbose_name_plural = 'Представитель детского дома'

    def __str__(self):
         return self.name


class Children(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', primary_key=True)
    profile_picture = models.ImageField(verbose_name='Аватар воспитаника', upload_to='children_avatars')
    patronymic = models.CharField(max_length=50, verbose_name='Отчество', null=True, blank=True)
    age = models.CharField(max_length=99, default=False, verbose_name='Возраст')
    sex = models.CharField(max_length=1, default=False, verbose_name='Пол')
    city = models.CharField(max_length=50, default=False,verbose_name='Город')
    children_home = models.ForeignKey(Director, on_delete=models.CASCADE, null=True,
                                      verbose_name='Название детского дома', related_name='director_children')

    class Meta:
        verbose_name = f'Воспитанник'
        verbose_name_plural = f'Воспитанники'

    def __str__(self):
        return self.user.first_name



