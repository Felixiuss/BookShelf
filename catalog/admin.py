from django.contrib import admin
from . models import Author, Category, Book, Language, Publisher


admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Publisher)


class BookInline(admin.TabularInline):
    model = Book
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_editable = ['date_of_birth']
    fields = ['first_name', 'last_name', 'bio', ('date_of_birth', 'date_of_death')]
    list_per_page = 10
    empty_value_display = '.......'
    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_category', 'pub_year', 'publisher')
    list_per_page = 20



