from django.contrib import admin

from .models import BlogCategory, BlogPost, BlogPostComment


class BlogPostCommentAdmin(admin.ModelAdmin):
    pass


class BlogPostCommentInlineAdmin(admin.TabularInline):
    model = BlogPostComment


class BlogCategoryAdmin(admin.ModelAdmin):
    search_fields = ("name", "description")

    prepopulated_fields = {"slug": ("name",)}


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published", "post_date")
    list_filter = ("published",)

    search_fields = ("title", "comment")

    prepopulated_fields = {"slug": ("title",)}

    inlines = (BlogPostCommentInlineAdmin,)


admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogPostComment, BlogPostCommentAdmin)
