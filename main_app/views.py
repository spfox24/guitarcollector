from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar, Case

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    return render(request, 'guitars/detail.html', { 'guitar': guitar })

class GuitarCreate(CreateView):
    model = Guitar
    fields = '__all__'

class GuitarUpdate(UpdateView):
    model = Guitar
    fields = ['model', 'serial', 'year', 'description']

class GuitarDelete(DeleteView):
    model = Guitar
    success_url = '/guitars/'

def cases_index(request):
    cases = Case.objects.all()
    return render(request, 'cases/index.html', { 'cases': cases })

def cases_detail(request, case_id):
    case = Case.objects.get(id=case_id)
    return render(request, 'cases/detail.html', { 'case': case })

class CaseCreate(CreateView):
    model = Case
    fields = '__all__'

class CaseUpdate(UpdateView):
    model = Case
    fields = '__all__'

class CaseDelete(DeleteView):
    model = Case
    success_url = '/cases/'




