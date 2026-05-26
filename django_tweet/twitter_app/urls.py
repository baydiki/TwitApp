from django.urls import path
from . import views
app_name = 'twitter_app'# Define the URL patterns for the twitter_app

urlpatterns = [
    path('', views.listtwits), #twit.com/ URL will be handled by the listtwits view
    path('listtwits/', views.listtwits, name='listtwits'),#twit.com/listtwits/ URL will be handled by the listtwits view
    path('addtwit/', views.addtwit, name='addtwit'),#twit.com/addtwit/ URL will be handled by the addtwit view
    path('addtwitbyform/', views.addTwitByForm, name='addtwitbyform'),#twit.com/addtwitbyform/ URL will be handled by the addTwitByForm view
    path('addtwitbymodelform/', views.addTwitByModelForm, name='addtwitbymodelform'),
]
