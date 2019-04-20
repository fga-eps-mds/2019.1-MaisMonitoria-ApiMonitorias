from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from user_account.views import UserAccountViewset
from tutoring_session.views import TutoringSessionViewset
from tutoring_session.views import ReceiptViewset
from tutoring_session.views import SolicitationViewset

router = routers.DefaultRouter()
router.register(r'user', UserAccountViewset)
router.register(r'tutoring', TutoringSessionViewset)
router.register(r'solicitation', SolicitationViewset)
router.register(r'receipt', ReceiptViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]