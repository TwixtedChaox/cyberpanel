from django.urls import path
from . import views

urlpatterns = [
    path('', views.alias_manager, name='email_alias_manager'),
    path('fetch/', views.fetch_aliases, name='fetch_aliases'),
    path('add/', views.add_alias, name='add_alias'),
    path('delete/', views.delete_alias, name='delete_alias'),
]
