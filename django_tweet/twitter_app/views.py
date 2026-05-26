from django.shortcuts import render
from . import models
from .forms import AddTweetModelForm, TweetForm
from django.shortcuts import redirect
from django.urls import reverse

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
        return redirect(reverse('twitter_app:listtwits'))
    return render(request, 'twitter_app/addtwit.html')
def addTwitByForm(request):
    if request.method == 'POST': # Check if the request method is POST
        form = TweetForm(request.POST) # Create a TweetForm instance with the POST data
        if form.is_valid(): # Check if the form is valid
            nickname = form.cleaned_data['nickname'] # Get the nickname from the form
            message = form.cleaned_data['content']
            twit = models.Twit(nickname=nickname, content=message) # Create a Twit object with the nickname and message
            twit.save() # Save the Twit object to the database
            return redirect(reverse('twitter_app:listtwits'))
        else:
            print("Form is not valid")
            return render(request, 'twitter_app/addtwitbyform.html', {'form': form})
    else:
        # If the request method is not POST, create an empty TweetForm instance
        return render(request, 'twitter_app/addtwitbyform.html', {'form': TweetForm()}) # Render the addtwitbyform.html template with an empty form instance
    
def addTwitByModelForm(request):
    if request.method == 'POST': # Check if the request method is POST
        form = AddTweetModelForm(request.POST) # Create an AddTweetModelForm instance with the POST data
        if form.is_valid(): # Check if the form is valid
            form.save() # Save the form data to create a new Twit object in the database
        return redirect(reverse('twitter_app:listtwits')) # Redirect to the listtwits view after saving
    else:
        return render(request, 'twitter_app/addtwitbymodelform.html', {'form': AddTweetModelForm()}) # Render the addtwitbymodelform.html template with an empty form instance