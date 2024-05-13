from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    text="merhaba"
    context = {"text": text}
    return render(request, "index.html", context)