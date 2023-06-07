from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/auth/login')
def AdminHomePage(request):
    if request.user.is_admin or  request.user.is_admin:  
        return render(request, 'siteadmin/home.html')
    else: 
        return render(request, '404.html')


@login_required(login_url='/auth/login')
def SettingPage(request):
    if request.user.is_admin or request.user.is_admin:  
        return render(request, 'siteadmin/setting.html')
    else: 
        return render(request, '404.html')


