from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
class Myview(View):
    name='predator'
    def get(self,request):
        return HttpResponse(self.name)

#making child of MyView class
class Myviewchild(Myview):
    def get(self,request):
        return HttpResponse(self.name)

#now we see the get post method of class based view 
class Myform(View):
    # if request.Method=='POST':
      def get(self,request):
        fm=ContactForm()
        return render(request,'app/contact.html',{'fm':fm})
      def post(self,request):
        fm=ContactForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            # fm.save()
        return render(request,'app/contact.html',{'fm':fm})



