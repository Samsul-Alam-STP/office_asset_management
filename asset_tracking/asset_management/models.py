from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField('Employee')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=50, unique=True)
    purchase_date = models.DateField()
    condition = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class CheckOut(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkout_date = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.device.name} checked out by {self.employee.name}"

class CheckIn(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField(auto_now_add=True)
    condition = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.device.name} checked in by {self.employee.name}"

