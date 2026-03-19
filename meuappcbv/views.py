from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

class HelloView(View):
    def get(self, request):
        return HttpResponse('Hello, Worlllld!')



# Create your views here.
