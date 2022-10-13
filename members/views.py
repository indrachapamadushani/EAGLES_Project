from django.shortcuts import render
from django.http import HttpResponse
from django.contib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url='signin')
def search(request):
    return render(request, 'serach.html')

                


