from django.shortcuts import render
from rest_framework import viewsets
from .models import book
from .serializers import BookSerializer
from django.core import serializers
from .forms import bookForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser



# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = book.objects.all()
    serializer_class = BookSerializer



def book_list(request):

    if request.method == 'GET':
        quer = book.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = BookSerializer(quer,context= serializer_context)
        return JsonResponse(serializer.data)

def book_detail(request, pk):
	book = get_object_or_404(book, pk=pk)
	return render(request, 'book_detail.html', {'books': book})

def another(request):
	list = book.objects.all()
	json_serializer = serializers.get_serializer("json")()
	response =  json_serializer.serialize(list, ensure_ascii=False, indent=2)
	return HttpResponse(response)

def add(request):
	if request.method == "POST":
		form = bookForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.save()
			return redirect('/books')
	else:
		form = bookForm
	return render(request, 'book_edit.html', {'form': form})


