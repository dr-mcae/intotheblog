from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class BlogCategory(models.Model):
    name = models.CharField(verbose_name=_("Title"), max_length=120)
    slug = models.SlugField()

    description = models.TextField(verbose_name=_("Description"), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Blog Category")
        verbose_name_plural = _("Blog Categories")
        ordering = ("slug",)


class BlogPostManager(models.Manager):
    def published(self):
        return self.filter(published=True)


class BlogPost(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=120)
    slug = models.SlugField()

    author = models.ForeignKey(
        verbose_name=_("Author"),
        to=get_user_model(),
        on_delete=models.SET_NULL,
        related_name="blog_posts",
        null=True,
    )
    category = models.ForeignKey(
        verbose_name=_("Category"),
        to="BlogCategory",
        on_delete=models.SET_NULL,
        related_name="posts",
        null=True,
    )

    post_date = models.DateTimeField(verbose_name=_("Post Date"), default=timezone.now)
    published = models.BooleanField(verbose_name=_("Published"), default=True)

    image = models.ImageField(upload_to='blog-images/', blank=True)

    content = models.TextField(verbose_name=_("Content"), blank=True)

    objects = BlogPostManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Blog Post")
        verbose_name_plural = _("Blog Posts")
        ordering = ("-post_date",)


class BlogPostCommentManager(models.Manager):
    def visible(self):
        return self.filter(visible=True)


class BlogPostComment(models.Model):
    post = models.ForeignKey(
        verbose_name=_("Post"),
        to="BlogPost",
        on_delete=models.SET_NULL,
        related_name="comments",
        blank=True,
        null=True,
    )

    comment_date = models.DateTimeField(
        verbose_name=_("Comment Date"), auto_now_add=True
    )

    visible = models.BooleanField(verbose_name=_("Visible"), default=True)
    name = models.CharField(verbose_name=_("Name"), max_length=120)
    comment = models.TextField(verbose_name=_("Comment"))

    objects = BlogPostCommentManager()

    def __str__(self):
        return f"Comment on post #{self.post_id} by {self.name}"

    class Meta:
        verbose_name = _("Blog Post Comment")
        verbose_name_plural = _("Blog Post Comments")
        ordering = ("post_id", "-comment_date")
