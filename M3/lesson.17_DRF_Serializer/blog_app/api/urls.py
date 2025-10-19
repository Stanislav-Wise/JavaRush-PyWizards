from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import DefaultRouter
from blog_app.api.views import PostViewSet


app_name = 'blog_api'
router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')  #api/v1/posts...
# router.register(r'commets', PostViewSet, basename='post')  #api/v1/posts...
# router.register(r'authors', PostViewSet, basename='post')  #api/v1/posts...

# /api/v1/token/
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
