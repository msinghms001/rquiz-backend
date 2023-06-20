from rest_framework.routers import SimpleRouter,DefaultRouter
router1=DefaultRouter()

from .views.Landing import Landing
router1.register(prefix='our_land',viewset=Landing,basename='simple')

urlpatterns = router1.urls