from django.contrib import admin
from django.urls import path

from api_monitoria import views as api_views

from rest_framework import routers


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/', api_views.TaskList.as_view(), name='task-list'),
]