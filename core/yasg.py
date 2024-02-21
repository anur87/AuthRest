from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions


''' schema view - это функия для отображения документации с использованием SwaggerUi '''
schema_view = get_schema_view(
    openapi.Info(
        title='Aut API',
        default_version='v1',
        description='Aut API',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='contact@snippets.local'),
        license=openapi.License(name='BSD License'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,), # Для отображения документации доступны все пользователи
)

''' urlpatterns - это список адресов, которые должны обрабатываться SwaggerUi'''
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('openapi/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]