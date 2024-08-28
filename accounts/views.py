from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
def register(request):
    if request.method != "POST":
        # Display a blank registration form
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        # Process the data
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("learning_logs:topics")
        
    context = {"form": form}
    return render(request, "registration/register.html", context)
