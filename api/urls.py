from django.contrib import admin
from django.urls import path

from api_monitoria import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/task/', api_views.TaskList.as_view(), name='task-list'),
]