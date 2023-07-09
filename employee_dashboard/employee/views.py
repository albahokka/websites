from django.shortcuts import render
from django.views.generic.base import View
from .models import Employee, Action
from .forms import EmployeeForm


# class EmployeesView(View):
#     def get(self, request):
#         form = EmployeeForm(request.GET or None)  # Создать экземпляр формы и передать GET-параметры, если они есть
#
#         if form.is_valid():
#             selected_employee = form.cleaned_data['employee']
#             selected_month = form.cleaned_data['month']
#             employees = Employee.objects.filter(full_name=selected_employee)
#             actions = Action.objects.filter(employee__full_name=selected_employee, month=selected_month)
#         else:
#             employees = Employee.objects.none()  # Инициализация переменной employees при невалидной форме
#             actions = Action.objects.none()
#
#         context = {'employees_list': employees, 'actions_list': actions, 'form': form}
#         return render(request, 'employee/employee.html', context)


class EmployeesView(View):
    def get(self, request):
        form = EmployeeForm(request.GET or None)

        if form.is_valid():
            selected_employee = form.cleaned_data['employee']
            selected_month = form.cleaned_data['month']
            employees = Employee.objects.filter(full_name=selected_employee)
            actions = Action.objects.filter(
                employee__full_name=selected_employee, month=selected_month)

            # Вычисление количества выполненных и невыполненных задач
            completed_tasks = sum(action.countt for action in actions)
            total_tasks = sum(action.target_count for action in actions)
            failed_tasks = total_tasks - completed_tasks

            # Вычисление процентов выполненных и невыполненных задач
            completed_percentage = round((completed_tasks / total_tasks) * 100,
                                         2) if total_tasks != 0 else 0
            failed_percentage = round((failed_tasks / total_tasks) * 100,
                                      2) if total_tasks != 0 else 0

            context = {
                'employees_list': employees,
                'actions_list': actions,
                'form': form,
                'completed_tasks': completed_tasks,
                'failed_tasks': failed_tasks,
                'total_tasks': total_tasks,
                'completed_percentage': completed_percentage,
                'failed_percentage': failed_percentage,
            }
        else:
            context = {
                'employees_list': Employee.objects.none(),
                'actions_list': Action.objects.none(),
                'form': form,
            }

        return render(request, 'employee/employee.html', context)


