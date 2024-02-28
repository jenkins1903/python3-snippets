# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('about/', views.about, name='about'),
# ]
# urlpatterns = [
#     path('item/<int:id>/', views.item, name='item'),
#     path('items/', views.items_list, name='items_list'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<int:id>/', views.item, name='item'),
    path('items/', views.items_list, name='items_list')
]