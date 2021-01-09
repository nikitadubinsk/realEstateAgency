from django.contrib import admin
from .models import Realtor, Position

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class RealtorResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = Realtor

class RealtorAdmin(ImportExportModelAdmin):
  list_display = ("id", "name", "email", "telephone", "position")
  list_display_links = ("name",)
  list_filter = ("position", )
  resource_class = RealtorResource

admin.site.register(Realtor, RealtorAdmin)

class PositionResource(resources.ModelResource):
  """Объявления для импорта"""
  class Meta:
    model = Position

class PositionAdmin(ImportExportModelAdmin):
  list_display = ("id", "title", "description")
  list_display_links = ("title",)
  resource_class = PositionResource

admin.site.register(Position, PositionAdmin)