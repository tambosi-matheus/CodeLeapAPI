from django.urls import path
from .views import ItemListCreate, ItemRetrieveUpdateDestroy

urlpatterns = [
    path('careers/', ItemListCreate.as_view()),
    path('careers/<int:pk>/', ItemRetrieveUpdateDestroy.as_view()),
]