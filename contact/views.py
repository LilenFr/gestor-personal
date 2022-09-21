from ast import Return
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContacForm
from django.contrib import messages


def index(request, letter=None):
    if letter != None:
        contacts = Contact.objects.filter(name__istartswith=letter)
    else:
        contacts = Contact.objects.filter(name__contains=request.GET.get('search', ''))
        
    context = {'contacts': contacts}
    return render(request, 'contact/index.html', context)


def view(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        'contact': contact
    }
    return render(request, 'contact/detail.html', context)


def edit(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == 'GET':
        form = ContacForm(instance=contact)
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'contact/edit.html', context)
    
    if request.method == 'POST':
        form = ContacForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
        messages.success(request, 'Contacto actualizada.')
        context = {
            'form': form,
            'id': id
        }
        return render(request, 'contact/edit.html', context)


def create(request):
    if request.method == 'GET':
        form = ContacForm()
        context = {
            'form': form
        }
        return render(request, 'contact/create.html', context)

    if request.method == 'POST':
        form = ContacForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('contact')


def delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect('contact')
