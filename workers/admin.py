from django.contrib import admin
from .models import Realtor, Position

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html, urlencode
from django.urls import reverse

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class PositionInUser(admin.StackedInline):
  model = Position
  can_delete = False
  verbose_name_plural = 'Позиция'
  verbose_name_plural = 'Позиции'

class MyUserAdmin(BaseUserAdmin):
  inlines = (PositionInUser,)
  list_display = ("id", "username", "first_name", "last_name", "is_staff", "position_link")

  def position_link(self, obj):
    url = (reverse("admin:workers_position_changelist") + "?" + urlencode({"courses__id": f"{obj.id}"}))
    return format_html('<a href="{}">{} user</a>', url, obj.position)
  
  position_link.short_description = "Позиция"


admin.site.unregister(User)
admin.site.register(User, MyUserAdmin)

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