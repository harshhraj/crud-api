from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.INDEX,name='home'),
    path('add',views.ADD,name='add'),
    path('edit',views.Edit,name='edit'),
    path('update/<str:id>',views.update,name='update'),
    path('delete/<str:id>',views.Delete,name='delete'),

    
]
