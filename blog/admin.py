from django.contrib import admin
from . models import *


admin.site.register(PostComment)
admin.site.register(Tag)


class PostCommentsInline(admin.TabularInline):
    model = PostComment
    max_num = 1
    # extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date_pub')
    inlines = [PostCommentsInline]
