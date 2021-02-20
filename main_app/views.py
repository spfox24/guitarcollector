import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar, Case, Photo
from .forms import PracticeForm

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'fox-guitarcollector'

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

def assoc_case(request, guitar_id, case_id):
    Guitar.objects.get(id=guitar_id).cases.add(case_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

def remove_case(request, guitar_id, case_id):
    Guitar.objects.get(id=guitar_id).cases.remove(case_id)
    return redirect('guitars_detail', guitar_id=guitar_id)

class GuitarCreate(CreateView):
    model = Guitar
    fields = ['brand', 'model', 'serial', 'year', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

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




