from django.shortcuts import render
from django.shortcuts import HttpResponse
from  book import models
from  book import douban
def ll(requset):
    return render(requset,'zhu.html')