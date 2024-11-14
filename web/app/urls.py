from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('add', views.add, name='add'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
    path('information', views.information, name='information'),
    path('contacts', views.contacts, name='contacts'),
]
