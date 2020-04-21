from django.shortcuts import render

# Create your views here.
def index(request,id,idTwo,idThree):
    return render(request,'index.html')