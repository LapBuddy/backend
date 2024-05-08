from django.contrib import admin
from django.urls import include, path
from accounts.views import UserViewset
from other.views import PostViewset, SessionViewset, SetupViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', UserViewset)
router.register(r'posts', PostViewset)
router.register(r'sessions', SessionViewset)
router.register(r'setups', SetupViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include('rest_framework.urls'))
]
