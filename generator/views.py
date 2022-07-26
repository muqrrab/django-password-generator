from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

"""
def home(request):                      #request is a paramter that must be given
    return HttpResponse('<h1>Hello World!!</h1>')
    """


#these are views whch will automatically goes to 'templates' folder and select the url as generator/home.html
#def home(request):
#    return render(request, 'generator/home.html')


#we can also pass differnet parameters to views like dictionaries
def home(request):
   return render(request, 'generator/home.html', {'password': 'asdasdsasass'})

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!@#~%$&*()'))

    if request.GET.get('number'):
        characters.extend(list('1234567890'))

    #everything provided in urls is string
    length = int(request.GET.get('length', 12))     #default is 12
    password = ""

    for x in range(length):
        password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': password})


