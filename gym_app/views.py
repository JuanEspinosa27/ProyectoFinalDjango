from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Member, Trainer, Class
from .forms import MemberForm, TrainerForm, ClassForm, SearchForm

def home(request):
    return render(request, 'gym_app/home.html')

def member_list(request):
    members = Member.objects.all()
    return render(request, 'gym_app/member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'gym_app/add_member.html', {'form': form})

def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'gym_app/trainer_list.html', {'trainers': trainers})

def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'gym_app/add_trainer.html', {'form': form})

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'gym_app/class_list.html', {'classes': classes})

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'gym_app/add_class.html', {'form': form})

def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            members = Member.objects.filter(
                Q(name__icontains=query) | Q(email__icontains=query)
            )
            trainers = Trainer.objects.filter(
                Q(name__icontains=query) | Q(specialization__icontains=query)
            )
            classes = Class.objects.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )
            return render(request, 'gym_app/search_results.html', {
                'members': members,
                'trainers': trainers,
                'classes': classes,
                'query': query,
                'form': form
            })
    else:
        form = SearchForm()
    return render(request, 'gym_app/search.html', {'form': form})