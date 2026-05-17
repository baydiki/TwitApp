from django.shortcuts import render
from . import models

# Create your views here.
def listtwits(request):
    all_twits = models.Twit.objects.all() # Retrieve all Twit objects from the database
    twit_dict = {'twits': all_twits} # Create a dictionary to pass the twits to the template
    return render(request, 'twitter_app/listtwit.html',context=twit_dict) # Render the listtwit.html template with the twits context

def addtwit(request):
    if request.method == 'POST': # Check if the request method is POST
        nickname = request.POST['nickname'] # Get the nickname from the form
        message = request.POST['message'] # Get the message from the form
        twit = models.Twit(nickname=nickname, content=message) # Create a Twit object with the nickname and message
        twit.save() # Save the Twit object to the database
        return listtwits(request) # Bu kısımda, yeni eklenen twiti listelemek için listtwits fonksiyonunu çağırıyoruz
    return render(request, 'twitter_app/addtwit.html')