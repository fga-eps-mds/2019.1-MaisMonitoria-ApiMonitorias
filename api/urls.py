from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from user_account.views import UserAccountViewset
from tutoring_session.views import TutoringSessionViewset

router = routers.DefaultRouter()
router.register(r'user', UserAccountViewset)
router.register(r'tutoring', TutoringSessionViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]