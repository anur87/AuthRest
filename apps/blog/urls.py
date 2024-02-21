from rest_framework.routers import DefaultRouter
from .views import BlogViewSet


router = DefaultRouter()
router.register('blog', BlogViewSet)


urlpatterns = router.urls
