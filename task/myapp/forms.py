from django import forms
from myapp.models import Employee, ExpenseLine, Expense


class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("name", "department", "job_title", "employee_status", "gender", "email", "phone", "marital_status")


class ExpenseLineForm(forms.ModelForm):
    class Meta:
        model = ExpenseLine
        fields = "__all__"


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ("reference", "description", "stage", "date", "employee", "total_amount")
