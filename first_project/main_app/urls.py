 
from django.urls import path
from .views import index

urlpatterns = [
    path('gg',index,name='index_page')
]