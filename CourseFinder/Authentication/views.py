from django.shortcuts import render,HttpResponse

# Create your views here.
def logIn(request):
    if request.method == 'GET':
        return render( request, 'logIn.html' )
    else:
        return HttpResponse("<h1><center>Successfull</center></h1>")


def signUp(request):
     if request.method == 'GET':
        return render( request, 'signUp.html' )
     else:
        return HttpResponse("<h1><center>Successfull</center></h1>")
