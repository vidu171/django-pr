from rest_framework import serializers
from .model import book

class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Post
		fields=('url','title','author')