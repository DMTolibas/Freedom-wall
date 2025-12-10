from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Rant
from .forms import RantForm

# Create your views here.
def index(request):

    form = RantForm()

    rants = Rant.objects.all()

    if request.method == 'POST':
        
        form = RantForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect('/')


    context = {'rants': rants, 'rantform': form}
    
    return render(request, "index.html", context)
