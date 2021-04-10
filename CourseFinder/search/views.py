from django.shortcuts import render,HttpResponse
from .models import base

# Create your views here.
def mainPage(request):
    if request.method == "GET":
        return render( request, 'search.html' )
    else:

        content = request.POST.get('content')
        duration = request.POST.get('duration')
        money = request.POST.get('money')

        duration = int(duration)

        arr = base.objects.filter(keyword=content,KeyDuration=duration)

        for i in arr:
            print(i.Link)
        
        return render( request , 'results.html' , {
            'val' : arr
        })
