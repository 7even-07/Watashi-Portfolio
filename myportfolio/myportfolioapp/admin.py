from django.contrib import admin
from .models import Tag, Project, ContactDetails

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ("name", "tags")
#     list_filter = ("tags",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "get_tags")
    list_filter = ("tags",)
    filter_horizontal = ("tags",)

    def get_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())

    get_tags.short_description = "Tags"

@admin.register(ContactDetails)
class ContactDetailsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)