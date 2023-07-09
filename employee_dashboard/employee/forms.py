from django import forms
from .models import Employee


class EmployeeForm(forms.Form):
    employee_choices = [(employee.full_name, employee.full_name) for employee in Employee.objects.all()]
    employee = forms.ChoiceField(choices=employee_choices)
    month_choices = [('Январь', 'Январь'), ('Февраль', 'Февраль'),
                     ('Март', 'Март'), ('Апрель', 'Апрель'),
                     ('Май', 'Май'), ('Июнь', 'Июнь'), ('Июль', 'Июль'),
                     ('Август', 'Август'), ('Сентябрь', 'Сентябрь'),
                     ('Октябрь', 'Октябрь'), ('Ноябрь', 'Ноябрь'),
                     ('Декабрь', 'Декабрь')]
    month = forms.ChoiceField(choices=month_choices)