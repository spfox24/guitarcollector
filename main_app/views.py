import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Guitar, Case, Photo
from .forms import PracticeForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'fox-guitarcollector'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid Sign Up'

    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def guitars_index(request):
    guitars = Guitar.objects.filter(user=request.user)
    return render(request, 'guitars/index.html', { 'guitars': guitars })

@login_required
def guitars_detail(request, guitar_id):
    guitar = Guitar.objects.get(id=guitar_id)
    cases_excluded = Case.objects.exclude(id__in = guitar.cases.all().values_list('id'))
    practice_form = PracticeForm()
    return render(request, 'guitars/detail.html', { 'guitar': guitar, 'practice_form': practice_form, 'cases': cases_excluded })

@login_required
def add_practice(request, guitar_id):
    form = PracticeForm(request.POST)
    if form.is_valid():
        new_practice = form.save(commit=False)
        new_practice.guitar_id = guitar_id
        new_practice.save()
    return redirect('guitars_detail', guitar_id=guitar_id)

@login_required
def add_photo(request, guitar_id):
    photo_file = request.FILES.get('photo_file', None)
    if photo_file:
        s3 = boto3.client('s3')
        index_of_last_period = photo_file.name.rfind('.')
        key = uuid.uuid4().hex[:6] + photo_file.name[index_of_last_period:]

        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, guitar_id=guitar_id)
            photo.save()
        except:
            print('An error occured uploading file to AWS')
    return redirect('guitars_detail', guitar_id=guitar_id)

@login_required
def remove_photo(request, guitar_id, photo_id):
    Guitar.objects.get(id=guitar_id).photo.remove(photo_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

@login_required
def assoc_case(request, guitar_id, case_id):
    Guitar.objects.get(id=guitar_id).cases.add(case_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

@login_required
def remove_case(request, guitar_id, case_id):
    Guitar.objects.get(id=guitar_id).cases.remove(case_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

class GuitarCreate(LoginRequiredMixin, CreateView):
    model = Guitar
    fields = ['brand', 'model', 'serial', 'year', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class GuitarUpdate(LoginRequiredMixin, UpdateView):
    model = Guitar
    fields = ['model', 'serial', 'year', 'description']

class GuitarDelete(LoginRequiredMixin, DeleteView):
    model = Guitar
    success_url = '/guitars/'

@login_required
def cases_index(request):
    cases = Case.objects.filter(user=request.user)
    return render(request, 'cases/index.html', { 'cases': cases })

@login_required
def cases_detail(request, case_id):
    case = Case.objects.get(id=case_id)
    return render(request, 'cases/detail.html', { 'case': case })

class CaseCreate(LoginRequiredMixin, CreateView):
    model = Case
    fields = ['case', 'brand']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CaseUpdate(LoginRequiredMixin, UpdateView):
    model = Case
    fields = ['case', 'brand']

class CaseDelete(LoginRequiredMixin, DeleteView):
    model = Case
    success_url = '/cases/'




