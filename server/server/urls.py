from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from MelodySync.views.PostView import PostViewSet
from MelodySync.views.UserView import UserViewSet
from MelodySync.views.ContactView import ContactView

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
