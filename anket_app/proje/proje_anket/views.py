from multiprocessing import context
from django.shortcuts import redirect, render

from .forms import  CreateCevaplarForm, CreateUserForm

from .models import Cevaplar, User, model_soru_secenek

# Create your views here.

def anket(request, user_id):
    user = User.objects.get(id=user_id)
    sorular = model_soru_secenek
    if request.method == 'POST':
        form = CreateCevaplarForm(request.POST)
        print("a")
        if form.is_valid():
            form.save()
            print("a")
            print(form.data)
            return redirect('kayit')
    else:
        form = CreateCevaplarForm()
    context = {
        'form' : form,
        'user': user,
        'sorular' : sorular,
    }
            
    return render(request, 'proje_anket/anket.html', context)
    
def kayit(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user= User.objects.last()
            return redirect('anket/' + str(user.id))
    else:
        form = CreateUserForm()
    context = {
        'form' : form
    }
    
    return render(request, 'proje_anket/kayit.html', context)

def analiz(request):
    context = {
        'sorular' : model_soru_secenek,
        'cevaplar': Cevaplar.objects.all()
    }
    return render(request, 'proje_anket/analiz.html', context)