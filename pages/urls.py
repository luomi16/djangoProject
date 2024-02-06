from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('page_not_found_view/', views.page_not_found_view,
         name='page_not_found_view')
]
