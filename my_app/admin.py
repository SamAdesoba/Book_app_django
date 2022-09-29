from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AdminUser

from .models import Book, Publisher, User


# Register your models here.
@admin.register(User)
class UserAdmin(AdminUser):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", 'first_name', 'last_name'),
            },
        ),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_published'
    list_display = ['title', 'price', 'isbn']
    list_editable = ['isbn']
    search_fields = ['title']
    list_filter = ['publisher', 'date_published']
    # fields = ['title', 'price', 'isbn']


# admin.site.register(Book, BookAdmin)
admin.site.register(Publisher)

