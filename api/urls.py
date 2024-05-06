from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PondokViewSet, SantriViewSet, PendaftaranViewSet

router = DefaultRouter()
router.register(r'pondoks', PondokViewSet)
router.register(r'santris', SantriViewSet)
router.register(r'pendaftarans', PendaftaranViewSet)

urlpatterns = router.urls
