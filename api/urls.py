from django.conf.urls.static import static
from django.conf.urls import include
from django.conf import settings
from django.contrib import admin
from django.urls import path

from rest_framework import routers

from tutoring_session.views import TutoringSessionViewset
from tutoring_session.views import SolicitationViewset
from tutoring_session.views import ReceiptViewset
from user_account.views import UserAccountViewset


router = routers.DefaultRouter()
router.register(r'user', UserAccountViewset)
router.register(r'tutoring', TutoringSessionViewset)
router.register(r'solicitation', SolicitationViewset)
router.register(r'receipt', ReceiptViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)