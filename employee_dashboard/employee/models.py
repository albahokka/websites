from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    months_worked = models.IntegerField()

    class Meta:
        db_table = 'employees'


class Action(models.Model):
    action_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, null=True)
    action_name = models.CharField(max_length=100, blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    countt = models.IntegerField(blank=True, null=True)
    target_count = models.IntegerField(blank=True, null=True)
    success_rate = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = 'actions'
