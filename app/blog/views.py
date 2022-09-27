from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView

from .forms import BlogPostCommentForm
from .models import BlogCategory, BlogPost


class HomePageView(ListView):
    model = BlogPost
    template_name = "blog/home_page.html"
    context_object_name = "blog_posts"

    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class BlogCategoryView(DetailView):
    model = BlogCategory
    context_object_name = "blog_category"


class BlogPostView(FormView, DetailView):
    model = BlogPost
    context_object_name = "blog_post"

    form_class = BlogPostCommentForm

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug=self.kwargs["category_slug"])

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.post = self.get_object()
        comment.save()

        return super().form_valid(form=form)
