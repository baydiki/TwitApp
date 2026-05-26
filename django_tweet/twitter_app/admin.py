from django.contrib import admin
from . import models
from twitter_app.models import Twit
# Register your models here.
class TwitAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Message Groups', {'fields': ['content']}),
        ('Author', {'fields': ['nickname']}),
        # Admin panelinde hangi alanların görüneceğini belirtiyoruz
    ]
    # fields=['nickname'] # Admin panelinde hangi alanların görüneceğini belirtiyoruz
admin.site.register(Twit, TwitAdmin) # Twit modelini admin paneline kaydediyoruz ve TwitAdmin sınıfını kullanarak özelleştiriyoruz
