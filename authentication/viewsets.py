from django.shortcuts import render
from rest_framework import viewsets

class CustomModelViewSets(viewsets.CustomModelViewSets)
 def get_serializer_class(self):
 	serializer_class