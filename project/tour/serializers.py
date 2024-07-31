from rest_framework import serializers
from .models import *


#Curd operation
class productseralizers(serializers.ModelSerializer):
    class Meta:
        model=Places
        fields='__all__'


