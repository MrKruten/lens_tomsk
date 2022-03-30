from django.urls import path
from .views import CategoryView

app_name = "categorys"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('categorys/', CategoryView.as_view()),
]