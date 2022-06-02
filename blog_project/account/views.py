from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def login(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
        return redirect('index')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html',{'form':form})
    
def logout(request):
    auth_logout(request)
    return redirect('index')