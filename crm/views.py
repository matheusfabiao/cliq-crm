from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .forms import (CreateRecordForm, CreateUserForm, LoginForm,
                    UpdateRecordForm)
from .models import Record
from .serializers import RecordSerializer


# Home page
def home(request):
    return render(request, 'crm/index.html')


# Register/Create a user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Conta criada com sucesso!')
            return redirect('login')
    context = {'form': form}
    return render(request, 'crm/register.html', context)


# Login a user
def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    context = {'form': form}
    return render(request, 'crm/login.html', context)


def user_logout(request):
    auth.logout(request)
    messages.success(request, 'Você foi desconectado!')
    return redirect('login')


# Dashboard
@login_required(login_url='login')
def dashboard(request):
    records = Record.objects.all()
    context = {'records': records}
    return render(request, 'crm/dashboard.html', context)


# CRUD
# Create a record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro criado com sucesso!')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'crm/create-record.html', context)


# Update a record
@login_required(login_url='login')
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registro atualizado com sucesso!')
            return redirect('dashboard')
    context = {'form': form}
    return render(request, 'crm/update-record.html', context)


# Read/View a record
@login_required(login_url='login')
def view_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record': record}
    return render(request, 'crm/view-record.html', context)


# Delete a record
@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Registro deletado com sucesso!')
    return redirect('dashboard')


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
