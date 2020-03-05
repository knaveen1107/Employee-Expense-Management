from django.db import models

Exp_stage = (
    ('Draft', 'Draft'),
    ('Submitted', 'Submitted'),
    ('Approved', 'Approved'),
    ('Paid', 'Paid'),
    ('Rejected', 'Rejected'),
    ('Cancelled', 'Cancelled')
)

Emp_status = (
    ('Trainee', 'Trainee'),
    ('Probation', 'Probation'),
    ('Permanent', 'Permanent'),
    ('NoticePeriod', 'NoticePeriod'),
    ('Contract', 'Contract'),
)

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

Marital_status = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Widow', 'Widow'),
    ('Divorced', 'Divorced')
)


class Department(models.Model):
    name = models.CharField(max_length=60, null=False)

    def __str__(self):
        return self.name


class JobTitle(models.Model):
    name = models.CharField(max_length=60, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=60, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    employee_status = models.CharField(max_length=50, choices=Emp_status, null=False)
    gender = models.CharField(max_length=20, choices=Gender, null=False)
    email = models.CharField(max_length=120, null=False)
    phone = models.CharField(max_length=60, null=False)
    marital_status = models.CharField(max_length=50, choices=Marital_status, null=False)

    def __str__(self):
        return self.name


class Expense(models.Model):
    reference = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length=120, null=False)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    total_amount = models.FloatField(null=False)
    stage = models.CharField(max_length=50, choices=Exp_stage, null=False)

    def __str__(self):
        return self.reference


class ExpenseLine(models.Model):
    item = models.CharField(max_length=60, null=False)
    description = models.CharField(max_length=120, null=False)
    quantity = models.IntegerField(null=False)
    price_unit = models.FloatField(null=False)
    total = models.FloatField(null=False)
    expense = models.ForeignKey(Expense, on_delete=models.CASCADE)

    def __str__(self):
        return self.item
