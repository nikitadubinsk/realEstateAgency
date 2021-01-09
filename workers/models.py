from django.db import models

class Realtor(models.Model): 
  name = models.CharField("Имя", max_length=300)
  email = models.CharField("Адрес электронная почта", max_length=300)
  telephone = models.CharField("Телефон", max_length=300)
  position = models.ForeignKey('Position', verbose_name="Должность", on_delete=models.SET_NULL, null=True)

  def __str__(self):
    return self.name

  class Meta: 
    verbose_name = "Риелтор"
    verbose_name_plural = "Риелторы"

class Position(models.Model): 
  title = models.CharField("Название", max_length=300)
  description = models.TextField("Описание")

  def __str__(self):
    return self.title

  class Meta: 
    verbose_name = "Должность"
    verbose_name_plural = "Должности"
