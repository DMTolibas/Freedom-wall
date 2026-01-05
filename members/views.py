from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            messages.success(request, ("Success!"))
            return redirect("home")
        else:
            # Return an 'invalid login' error message.
            messages.success(request, ("There is an error. Try again!"))
            return redirect("login")

    else:
        return render(request, "authentication/login.html", {})

def logout_user(request):
    logout(request) #actually log out the user
    # show meesage and redirect when log out
    messages.success(request, ("There is an error. Try again!"))
    return redirect("home")
