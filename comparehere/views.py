from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    # return HttpResponse("This is the main page of your compare here website.")
    return render(request, "main_index.html")