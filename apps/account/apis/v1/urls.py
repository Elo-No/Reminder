from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.apis.v1.views import ObtainTokenPairView, RegisterView

urlpatterns = [
    path('login/', ObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]