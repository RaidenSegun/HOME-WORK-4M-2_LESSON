from django.shortcuts import render
from bunner.models import Bunner

# Create your views here.
def bunner(requset):
    bunner = Bunner.objects.all()
    return render(requset, 'index2.html', locals())