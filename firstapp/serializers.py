from django import forms
from rest_framework import serializers

from .models import Contact,BlogPost

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields='__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        #fields='__all__'
        fields=['id','name','messenger','sender']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=BlogPost
        #fields="__all__"
        exclude=['is_active']
