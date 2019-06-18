from django.shortcuts import render
from django.shortcuts import HttpResponse
from  book import models
from  book import douban
# Create your views here.
def openbook(request):
    flag=0
    a,b,c,d=douban.getdetiles()
    ls = models.bookdetils.objects.all()
    for i in ls :
        if(i.id==1):
            flag=1
            break
    if(flag==0):
        for i in range(len(a)):
            models.bookdetils.objects.create(id=i,title=a[i],tiems=b[i],detile=d[i],imgs=c[i])
    ls = models.bookdetils.objects.all()
    return render(request,'index.html',{'li':ls})
