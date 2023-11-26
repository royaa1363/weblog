from django.contrib import admin

from blog.models import Post, Comment, Category, Tag, Like

# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Like)


class CommentInLineAdmin(admin.StackedInline):
    model = Comment
    fields = ['user', 'post', 'text']
    extra = 0


class LikeInLineAdmin(admin.StackedInline):
    model = Like
    fields = ['user', 'is_liked']
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'pub_date']
    filter_horizontal = ['tags']
    search_fields = ('categories__title',)
    inlines = [CommentInLineAdmin, LikeInLineAdmin]




