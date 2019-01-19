from django.contrib import admin
from . models import *


# admin.site.register(Post)
admin.site.register(PostComment)
admin.site.register(Tag)


class PostCommentsInline(admin.TabularInline):
    """ Used to show 'existing' blog comments inline below associated blogs """
    model = PostComment
    max_num = 1
    # extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Administration object for Blog models.
    Defines:
     - fields to be displayed in list view (list_display)
     - orders fields in detail view (fields), grouping the date fields horizontally
     - adds inline addition of blog comments in blog view (inlines)
    """
    list_display = ('title', 'author', 'date_pub')
    inlines = [PostCommentsInline]
