from django.shortcuts import render
from django.views.generic import View


class MyViewClass(View):
    def get(self,req,*args,**kwargs):
        return render(req,'pages/signup.html')
        #return render(req,'home/index.html')
