from django.contrib import admin

# Register your models here.
from .models import Notes , NewNote

admin.site.register(Notes)
admin.site.register(NewNote)
