from django.urls import path

from .views import CatListView,CatDetailView

urlpatterns = [
        path('',CatListView.as_view(),name='cat_list'),
        path('<uuid:pk>',CatDetailView.as_view(),name='cat_detail'),
        ]
