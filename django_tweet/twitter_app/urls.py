from django.urls import path
from . import views
app_name = 'twitter_app'# Define the URL patterns for the twitter_app

urlpatterns = [
    path('listtwits/', views.listtwits, name='listtwits'),#twit.com/listtwits/ URL will be handled by the listtwits view
    path('addtwit/', views.addtwit, name='addtwit'),#twit.com/addtwit/ URL will be handled by the addtwit view
]
