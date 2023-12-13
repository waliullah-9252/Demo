from django.urls import path,include
from .import views

urlpatterns = [
    path('add/', views.add_post, name = 'add_post'),
    path('edit/<int:id>', views.edit_post, name = 'edit_post'),
    path('delete/<int:id>', views.delete_post, name = 'delete_post'),
    path('complete_post/<int:id>', views.complete_post, name = 'complete_post'),
]