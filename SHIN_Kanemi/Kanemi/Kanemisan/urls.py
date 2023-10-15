from django.urls import path
from . import views

urlpatterns = [
    path("get_product_info/", views.get_product_info, name="get_product_info"),
]


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]

