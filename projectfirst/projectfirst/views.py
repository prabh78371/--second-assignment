# created by prabhjot kaur
from django.http import HttpResponse
from django.shortcuts import render

# views
def homepage(request):
    Name = {'name' : 'Prabhjot'}
    return render(request, 'priya.html', Name)


