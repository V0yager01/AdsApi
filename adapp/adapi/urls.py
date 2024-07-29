from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import AdViewSet, UserCreateViewSet


ad_v1_routes = DefaultRouter()
ad_v1_routes.register(
    'ads',
    AdViewSet,
    basename='ads'
)
ad_v1_routes.register(
    'user',
    UserCreateViewSet,
    basename='user'
)
urlpatterns = [
    path('v1/auth/token/', TokenObtainPairView.as_view()),
    path('v1/', include(ad_v1_routes.urls))
]
