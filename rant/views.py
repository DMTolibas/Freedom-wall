from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Rant
from .forms import RantForm

# Create your views here.
def index(request):

    form = RantForm()

    rants = Rant.objects.all()
    '''Obtain the most recent rant'''
    today_rant = Rant.objects.order_by('-created').first()  #this code obtain the latest obj. #order_by('-created').first means that in database, sort the data from newest to oldest. "-" means start at newest

    if request.method == 'POST':

        form = RantForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('/')


    context = {'rants': rants, 'rantform': form, 'today_rant': today_rant}
    
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")

def rule(request):
    return render(request, "rule.html")

def login(request):
    return render(request, "login.html")   

 