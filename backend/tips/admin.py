from django.contrib import admin

from .models import Tip


@admin.register(Tip)
class TipAdmin(admin.ModelAdmin):
    list_filter = ["user", "created_at"]
    search_fields = ["animal", "user", "content"]
    ordering = ["-updated_at"]
