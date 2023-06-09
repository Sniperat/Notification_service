from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Notification Service",
      default_version='v1',
      description="",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   #  path('refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', include('main.urls'))
]
