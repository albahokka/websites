from django.contrib import admin

from .models import Employee, Action


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'city', 'months_worked')


@admin.register(Action)
class ActionsAdmin(admin.ModelAdmin):
    list_display = ('action_id', 'employee', 'action_name', 'month',
                    'countt', 'target_count', 'success_rate')
