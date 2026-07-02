from django.urls import path
from . import views

urlpatterns = [
    path('recommend-box/<int:product_id>/', views.recommend_box_for_product, name='recommend_box'),
]