from django.urls import path, include
from rest_framework import routers
from . import views
from django.contrib import admin
from .views import BookmarkViewSet,CategoryViewSet,SearchViewSet


app_name = 'lime'


router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('uu', BookmarkViewSet)
router.register('ss', SearchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
