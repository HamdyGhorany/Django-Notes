from .models import Notes , NewNote
from rest_framework import routers, serializers, viewsets

class JsonNote(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'



class Json_New_Notes(serializers.ModelSerializer):
    class Meta:
        model = NewNote
        fields = '__all__'