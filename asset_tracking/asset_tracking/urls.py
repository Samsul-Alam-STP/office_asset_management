from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from asset_management.views import (
    CompanyViewSet,
    EmployeeViewSet,
    DeviceViewSet,
    CheckOutViewSet,
    CheckInViewSet,
)

router = routers.DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'devices', DeviceViewSet)
router.register(r'checkouts', CheckOutViewSet)
router.register(r'checkins', CheckInViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
