from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string

HTML_STRING = render_to_string ('index.html')

def index(request):
    return HttpResponse(HTML_STRING)