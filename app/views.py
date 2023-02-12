from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.
class Myview(View):
    name='predator'
    def get(self,request):
        return HttpResponse(self.name)

#making child of MyView class
class Myviewchild(Myview):
    def get(self,request):
        return HttpResponse(self.name)



