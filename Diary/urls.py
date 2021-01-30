from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.EntranceView.as_view(), name="Entrance"),
    path("aboutMe/", views.about, name="about"),
    path("aboutQuantumGun/", views.aboutQG, name="aboutQG"),
    path("blog/", views.allBlogList, name="blog"),

    path("blog/<str:SUBNAME>/", views.blogList, name="blogGenre"),
    path("blogDetail/<int:pk>/", views.BlogDetail, name="detail"),

]

