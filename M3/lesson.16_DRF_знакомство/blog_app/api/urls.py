from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView


app_name = 'blog_api'

# /api/v1/token/
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
