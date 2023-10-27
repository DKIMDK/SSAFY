from django.urls import path
from . import views


app_name = "finlife"
urlpatterns = [
    path("", views.index),

    # path("list_data", views.)
    # path("", views.)
    # path("hot_weathers/", views.hot_weathers, name=)
]
