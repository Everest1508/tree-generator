from django.urls import path, include
from .views import *
urlpatterns = [
    path('', dynamic_tree_view),
]
