from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.accept,name='accept'),
    path('<int:id>/',views.resume,name='resume'),
    path('list/',views.list,name='list'),
    path('delete/<int:id>', views.delete, name='delete'),
]
