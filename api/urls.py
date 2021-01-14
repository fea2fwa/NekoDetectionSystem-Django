from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from api.views import PostViewSet

router = routers.DefaultRouter()
router.register('cats', PostViewSet)

urlpatterns = [
        path ('',include(router.urls)),
        ]
