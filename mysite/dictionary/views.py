from django.shortcuts import render
from django.http import HttpResponse

from .models import Word

# Create your views here.
def index(request):
	words = Word.objects.all()
	context = {'words':words}
	return render(request, 'dictionary/index.html',context)