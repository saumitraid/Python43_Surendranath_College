from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>About us</h1>')

def contact(request):
    if request.GET:
        name=request.GET.get('name')
        email=request.GET.get('email_id')
        msg=request.GET.get('msg')
        context={'name':name,'email':email, 'msg':msg}
        return render(request, 'contact.html', context)
    else:
        return render(request, 'contact.html')
