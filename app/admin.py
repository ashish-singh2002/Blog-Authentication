from django.contrib import admin
from .models import Ashish
 

@admin.register(Ashish)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','content','timestamp']
