from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from TMS import views

router = routers.DefaultRouter()
router.register(r'tmss', views.TmsView, 'TMS')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]