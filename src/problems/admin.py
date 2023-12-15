from django.contrib import admin

from .models import (
    Theme,
    Problem,
    Comment,
)



@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    show_full_result_count = False


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    show_full_result_count = False

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    show_full_result_count = False
