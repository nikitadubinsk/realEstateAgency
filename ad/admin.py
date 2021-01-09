from django.contrib import admin

from .models import Ad, TypeOfAd, TypeOfArea, Developer, Author, Сonvenience, Rating, Price
from workers.models import Realtor, Position

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class AdResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = Ad

class AdAdmin(ImportExportModelAdmin):
  list_display = ("id", "title", "description", "address", "createdAt", "area", "floor", "constructionAt", "typeOfArea", "typeOfAd", "realtor", "done")
  list_display_links = ("title",)
  list_filter = ("typeOfArea", "typeOfAd",)
  search_fields = ("title",)
  save_on_top = True
  actions = ['publish', 'unpublish']
  resource_class = AdResource

  def unpublish(self, request, queryset):
    """Снять с публикации"""
    row_update = queryset.update(done=True)
    if row_update == 1:
      message_bit = "1 объявление было снято"
    else:
      message_bit = f"{row_update} объявлений были сняты"
    self.message_user(request, f"{message_bit}")

  unpublish.short_description = "Снять с публикации"
  unpublish.allowed_permissions = ('change',)
  
  def publish(self, request, queryset):
    """Опубликовать"""
    row_update = queryset.update(done=False)
    if row_update == 1:
      message_bit = "1 объявление было опубликовано"
    else:
      message_bit = f"{row_update} объявлений были опубликованы"
    self.message_user(request, f"{message_bit}")

  publish.short_description = "Опубликовать"
  publish.allowed_permissions = ('change',)
  
admin.site.register(Ad, AdAdmin)

class TypeOfAdResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = TypeOfAd

class TypeOfAdAdmin(ImportExportModelAdmin):
  list_display = ("id", "name")
  list_display_links = ("name",)
  resource_class = TypeOfAdResource

admin.site.register(TypeOfAd, TypeOfAdAdmin)

class TypeOfAreaResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = TypeOfArea

class TypeOfAreadAdmin(ImportExportModelAdmin):
  list_display = ("id", "name", "description")
  list_display_links = ("name",)
  resource_class = TypeOfAreaResource

admin.site.register(TypeOfArea, TypeOfAreadAdmin)

class DeveloperResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = Developer

class DeveloperAdmin(ImportExportModelAdmin):
  list_display = ("id", "name", "description", "createdAt")
  list_display_links = ("name",)
  resource_class = DeveloperResource

admin.site.register(Developer, DeveloperAdmin)

class AuthorResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = Author

class AuthorAdmin(ImportExportModelAdmin):
  list_display = ("id", "name", "birthday", "createdAt", "login")
  list_display_links = ("name",)
  resource_class = AuthorResource

admin.site.register(Author, AuthorAdmin)

class СonvenienceResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = Сonvenience

class СonvenienceAdmin(ImportExportModelAdmin):
  list_display = ("id", "title")
  list_display_links = ("title",)
  resource_class = СonvenienceResource

admin.site.register(Сonvenience, СonvenienceAdmin)

class RatingResource(ImportExportModelAdmin):
  """Объявления для импорта"""
  class Meta:
    model = Rating

class RatingAdmin(admin.ModelAdmin):
  list_display = ("id", "point", "ad", "author",)
  list_display_links = ("point", "ad",)
  list_filter = ("ad", "author",)
  resource_class = RatingResource

admin.site.register(Rating, RatingAdmin)

class PriceResource(ImportExportModelAdmin):
  """Объявления для импорта"""
  class Meta:
    model = Price

class PriceAdmin(admin.ModelAdmin):
  list_display = ("id", "ad", "newPricece", "updatedAt")
  list_display_links = ("ad", "newPricece",)
  list_filter = ("ad",)
  resource_class = PriceResource

admin.site.register(Price, PriceAdmin)