from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def signup_view(request):
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup')
    template_name='auth_app/signup_form.html'
    context={'form':form}
    return render(request, template_name, context)

def signin_view(request):
    if request.method=='POST':

        uname=request.POST.get('un')
        passw=request.POST.get('pw')

        user=authenticate(username=uname, password=passw)
        if user is not None:
            login(request,user)
            return redirect('student')

    template_name='auth_app/signin_form.html'
    context={}
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('signin')