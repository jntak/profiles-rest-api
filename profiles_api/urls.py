from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileFeedViewset, UserProfileViewSet, UserLoginAPIView


router = DefaultRouter()
router.register("users", UserProfileViewSet)
router.register("feed", UserProfileFeedViewset)


urlpatterns = [
    path("login/", UserLoginAPIView.as_view()),
    path("", include(router.urls)),
]
