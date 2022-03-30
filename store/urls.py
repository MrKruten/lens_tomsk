from django.urls import path
from .views import CategoryView, ProductView

app_name = "store"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('categories/', CategoryView.as_view()),
    path('products/', ProductView.as_view()),
]
