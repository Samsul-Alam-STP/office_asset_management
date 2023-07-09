from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Company, Employee, Device, CheckOut, CheckIn
from .serializers import (
    CompanySerializer,
    EmployeeSerializer,
    DeviceSerializer,
    CheckOutSerializer,
    CheckInSerializer,
)

class CompanyViewSet(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated]

class EmployeeViewSet(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

class DeviceViewSet(generics.ListCreateAPIView):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

class CheckOutViewSet(generics.ListCreateAPIView):
    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer
    permission_classes = [IsAuthenticated]

class CheckInViewSet(generics.ListCreateAPIView):
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = [IsAuthenticated]

class EmployeeDeviceAPIView(generics.ListAPIView):
    serializer_class = DeviceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Device.objects.filter(checkout__employee_id=employee_id)

class DeviceCheckOutAPIView(generics.ListAPIView):
    serializer_class = CheckOutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        device_id = self.kwargs['device_id']
        return CheckOut.objects.filter(device_id=device_id)

class CheckOutEmployeeAPIView(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        checkout_id = self.kwargs['checkout_id']
        return Employee.objects.filter(checkout__id=checkout_id)
