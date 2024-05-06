from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PondokViewSet

router = DefaultRouter()
router.register(r'pondoks', PondokViewSet)

urlpatterns = router.urls
