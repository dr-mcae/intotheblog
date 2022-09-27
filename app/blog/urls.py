from django.urls import path

from .views import BlogCategoryView, BlogPostView, HomePageView

urlpatterns = [
    path("<slug:slug>/", BlogCategoryView.as_view(), name="blog-category"),
    path("<slug:category_slug>/<slug:slug>/", BlogPostView.as_view(), name="blog-post"),
    path("", HomePageView.as_view(), name="home-page"),
]
