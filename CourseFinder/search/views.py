from django.shortcuts import render,HttpResponse

# Create your views here.
def mainPage(request):
    if request.method == "GET":
        return render( request, 'search.html' )
    else:
        return HttpResponse("Anything")
