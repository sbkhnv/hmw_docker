from django.urls import path
from .views import ProduceListView

urlpatterns = [
    path('products/',ProduceListView.as_view(),name='products'),
]