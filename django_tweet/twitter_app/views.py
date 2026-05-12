from django.shortcuts import render

# Create your views here.
def listtwits(request):
    return render(request, 'twitter_app/listtwit.html')

def addtwit(request):
    return render(request, 'twitter_app/addtwit.html')