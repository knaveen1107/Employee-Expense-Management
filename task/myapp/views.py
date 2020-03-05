from django.shortcuts import render, redirect
from myapp import forms


def empview(request):
    if request.method == 'POST':
        form = forms.EmpForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/emp')
            except:
                pass
    else:
        form = forms.EmpForm()
    return render(request, 'emp.html', {'form': form})


def explineview(request):
    if request.method == 'POST':
        form = forms.ExpenseLineForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/expline')
            except:
                pass
    else:
        form = forms.ExpenseLineForm()
    return render(request, 'expline.html', {'form': form})


def expview(request):
    if request.method == 'POST':
        form = forms.ExpenseForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/exp')
            except:
                pass
    else:
        form = forms.ExpenseForm()
    return render(request, 'exp.html', {'form': form})
