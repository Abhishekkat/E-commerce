from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="shop home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="Contact "),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("tracking/", views.tracking, name="tracking"),
    path("search/", views.search, name="search"),

]
