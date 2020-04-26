from django.urls import path
from . import views

urlpatterns = [
    path('create',views.create,name="create"),
    path('update/<str:pk>',views.update,name="update"),
    path('delete/<str:pk>',views.delete,name="delete"),
    path('post/<str:pk>',views.post,name="post"),
    path('',views.index,name="index")
]
