from django.contrib import admin
from .models import Expense, ExpenseLine, Employee, Department, JobTitle


admin.site.register(Expense)
admin.site.register(ExpenseLine)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(JobTitle)
