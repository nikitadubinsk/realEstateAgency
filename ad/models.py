from django.db import models
from workers.models import Realtor, Position

class Ad(models.Model): 
  title = models.CharField("Название", max_length=300)
  description = models.TextField("Описание")
  address = models.CharField("Адрес", max_length=400)
  createdAt = models.DateField("Дата создания объявления")
  area = models.PositiveSmallIntegerField("Площадь", default=0)
  floor = models.PositiveSmallIntegerField("Этаж", default=0)
  constructionAt = models.PositiveSmallIntegerField("Год постройки", default=2020)
  author = models.ForeignKey('Author', verbose_name="Автор объявления", on_delete=models.SET_NULL, null=True)
  typeOfArea = models.ForeignKey('TypeOfArea', verbose_name="Тип площади", on_delete=models.SET_NULL, null=True)
  typeOfAd = models.ForeignKey('TypeOfAd', verbose_name="Тип объявления", on_delete=models.SET_NULL, null=True)
  developer = models.ForeignKey('Developer', verbose_name="Застройщик", on_delete=models.SET_NULL, null=True)
  realtor = models.ForeignKey(Realtor, verbose_name="Риелтор", on_delete=models.SET_NULL, null=True)
  convenience = models.ManyToManyField('Сonvenience', verbose_name="Удобства")
  done = models.BooleanField("Статус")

  def __str__(self):
    return self.title

  class Meta: 
    verbose_name = "Объявление"
    verbose_name_plural = "Объявления"

class TypeOfAd(models.Model): 
  name = models.CharField("Тип объявления", max_length=300)

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Тип объявления"
    verbose_name_plural = "Типы объявления"

class TypeOfArea(models.Model): 
  name = models.CharField("Тип помещения", max_length=300)
  description = models.TextField("Описание")

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Тип помещения"
    verbose_name_plural = "Типы помещений"

class Developer(models.Model): 
  name = models.CharField("Название", max_length=300)
  description = models.TextField("Описание")
  createdAt = models.DateField("Дата начала работы")

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Застройщик"
    verbose_name_plural = "Застройщики"

class Author(models.Model): 
  name = models.CharField("Имя", max_length=300)
  createdAt = models.DateField("Дата регистрации")
  birthday = models.DateField("Дата рождения")
  login = models.CharField("Логин", max_length=300)
  password = models.CharField("Пароль", max_length=300)

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Автор"
    verbose_name_plural = "Авторы"

class Сonvenience(models.Model): 
  title = models.CharField("Название", max_length=300)

  def __str__(self):
    return self.title

  class Meta: 
    verbose_name = "Удобство"
    verbose_name_plural = "Удобства"

class Rating(models.Model): 
  point = models.CharField("Оценка", max_length=4)
  ad = models.ForeignKey('Ad', verbose_name="Объявление", on_delete=models.SET_NULL, null=True)
  author = models.ForeignKey('Author', verbose_name="Автор оценки", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.point

  class Meta: 
    verbose_name = "Рейтинг"
    verbose_name_plural = "Рейтинги"

class Price(models.Model): 
  updatedAt = models.DateField("Дата обновления")
  ad = models.ForeignKey('Ad', verbose_name="Объявление", on_delete=models.SET_NULL, null=True, related_name="price")
  newPricece = models.CharField("Стоимость", max_length=4)

  def __str__(self):
    return self.newPricece

  class Meta: 
    verbose_name = "Стоимость"
    verbose_name_plural = "Стоимости"