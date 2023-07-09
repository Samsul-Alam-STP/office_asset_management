from django.contrib import admin
from django.urls import path, include
from asset_management.views import (
    CompanyViewSet,
    EmployeeViewSet,
    DeviceViewSet,
    CheckOutViewSet,
    CheckInViewSet,
    EmployeeDeviceAPIView,
    DeviceCheckOutAPIView,
    CheckOutEmployeeAPIView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', CompanyViewSet.as_view(), name='company-list-create'),
    path('api/employees/', EmployeeViewSet.as_view(), name='employee-list-create'),
    path('api/devices/', DeviceViewSet.as_view(), name='device-list-create'),
    path('api/checkouts/', CheckOutViewSet.as_view(), name='checkout-list-create'),
    path('api/checkins/', CheckInViewSet.as_view(), name='checkin-list-create'),
    path('api/employees/<int:employee_id>/devices/', EmployeeDeviceAPIView.as_view(), name='employee-devices'),
    path('api/devices/<int:device_id>/checkouts/', DeviceCheckOutAPIView.as_view(), name='device-checkouts'),
    path('api/checkouts/<int:checkout_id>/employee/', CheckOutEmployeeAPIView.as_view(), name='checkout-employee'),
]
