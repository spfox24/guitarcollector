from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar, Case
from .forms import PracticeForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def guitars_index(request):
    guitars = Guitar.objects.all()
    return render(request, 'guitars/index.html', { 'guitars': guitars })

def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    cases_excluded = Case.objects.exclude(id__in = guitar.cases.all().values_list('id'))
    practice_form = PracticeForm()
    return render(request, 'guitars/detail.html', { 'guitar': guitar, 'practice_form': practice_form, 'cases': cases_excluded })

def add_practice(request, guitar_id):
    form = PracticeForm(request.POST)
    if form.is_valid():
        new_practice = form.save(commit=False)
        new_practice.guitar_id = guitar_id
        new_practice.save()
    return redirect('guitars_detail', guitar_id=guitar_id)

def assoc_case(request, guitar_id, case_id):
    Guitar.objects.get(id=guitar_id).cases.add(case_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

def remove_case(request, guitar_id, case_id):
    Guitar.objects.get(id=guitar_id).cases.remove(case_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['brand', 'model', 'serial', 'year', 'description']

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




