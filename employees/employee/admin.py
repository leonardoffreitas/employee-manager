from django.contrib import admin
from employees.employee.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    '''Admin Manager Features'''
    model = Employee
    list_display = ["name", "email", "department"]
    list_filter = ["department"]
    search_fields = ["name", "department"]
    save_on_top = True
admin.site.register(Employee, EmployeeAdmin)
