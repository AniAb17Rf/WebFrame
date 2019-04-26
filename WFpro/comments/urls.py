from django.urls import path
from . import views
urlpatterns = [
    path('', views.WT, name='WT'),
    path('horror', views.horror, name='horror'),
    path('scifi', views.scifi, name='scifi'),
    path('crime',views.crime, name='crime'),
    path('comments',views.comm, name='comm')
]