from django.contrib import admin

from .models import Hospital, Review


@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ["name", "call", "address", "created_at"]
    search_fields = ["name", "call", "address", "info", "created_at"]
    ordering = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["hospital", "user", "title", "grade", "created_at"]
    search_fields = ["hospital", "user", "title", "grade", "content"]
    ordering = ["-created_at"]
