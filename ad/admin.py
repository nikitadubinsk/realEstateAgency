from django.contrib import admin

from .models import Ad
from .models import TypeOfAd
from .models import TypeOfArea
from .models import Developer
from .models import Author
from .models import Сonvenience
from .models import Realtor
from .models import Position
from .models import Rating
from .models import Price

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
  # list_display = ("id", "title", "description", "address", "createdAt", "area", "floor", "convenience", "constructionAt", "typeOfArea", "typeOfAd", "done")
  list_display = ("id", "title", "description", "address", "createdAt", "area", "floor", "constructionAt", "typeOfArea", "typeOfAd", "done")
  list_display_links = ("title",)
  list_filter = ("typeOfArea", "typeOfAd",)
  search_fields = ("title",)
  save_on_top = True

@admin.register(TypeOfAd)
class TypeOfAdAdmin(admin.ModelAdmin):
  list_display = ("id", "name")
  list_display_links = ("name",)

@admin.register(TypeOfArea)
class TypeOfAreadAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "description")
  list_display_links = ("name",)

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "description", "createdAt")
  list_display_links = ("name",)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "birthday", "createdAt", "login")
  list_display_links = ("name",)

@admin.register(Сonvenience)
class СonvenienceAdmin(admin.ModelAdmin):
  list_display = ("id", "title")
  list_display_links = ("title",)

@admin.register(Realtor)
class RealtorAdmin(admin.ModelAdmin):
  list_display = ("id", "name", "email", "telephone", "position")
  list_display_links = ("name",)

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
  list_display = ("id", "title", "description")
  list_display_links = ("title",)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
  list_display = ("id", "point", "ad", "author",)
  list_display_links = ("point", "ad",)
  list_filter = ("ad", "author",)

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
  list_display = ("id", "ad", "newPricece", "updatedAt")
  list_display_links = ("ad", "newPricece",)
  list_filter = ("ad",)