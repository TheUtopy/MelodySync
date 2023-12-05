from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from MelodySync.views.post_view import PostViewSet
from MelodySync.views.user_view import UserViewSet
from MelodySync.views.contact_view import ContactView

router = routers.SimpleRouter()

router.register('user', UserViewSet, basename='user')
router.register('post', PostViewSet, basename='post')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('accounts/', include('django.contrib.auth.urls')),
]
