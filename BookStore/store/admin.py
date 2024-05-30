from django.contrib import admin
from . models import *

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    date_hierarchy = 'dob'
    empty_value_display = '/'
    fields = ['first_name', 'last_name', ('dob', 'age'), 'dod']
    readonly_fields = ['age']
    def upper_case_name(obj):
        return f"{obj.first_name}".capitalize() + " " + f"{obj.last_name}".capitalize()
    list_display = [upper_case_name, 'age']
    list_display_links = ['age']
    list_filter = ['first_name', 'last_name']
    ordering = ['dob']


admin.site.register(Author, AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    actions_selection_counter = False
    date_hierarchy = 'published'
    empty_value_display = '/'
    fieldsets = [
        (
            "Picture",
            {
                'fields' : ['cover_picture'],
                'description' : 'The picture will be saved in the media folder inside your project container directory'
            },
        ),
        (
            None,
            {
                'fields' : [('title', 'num_pages'), 'cover', 'genre']
            },
        ),
        (
            "Publishing Information",
            {
                'fields' : ['author', ('publisher', 'published')],
            }
        ),
        (
            "Availability",
            {
                'fields' : ['price', ('available_copies', 'sold_out')],
            }
        )
    ]
    list_display = ["title", "num_pages", "cover", "genre", "published", "publisher", "author", 'price', 'available_copies', 'sold_out']
    list_filter = ['genre']
    radio_fields = {'cover': admin.HORIZONTAL}
    search_fields = ['title']

admin.site.register(Book, BookAdmin)

class PublisherAdmin(admin.ModelAdmin):
    fields = ['name', ('address', 'city'), ('state_province', 'country')]

admin.site.register(Publisher, PublisherAdmin)
