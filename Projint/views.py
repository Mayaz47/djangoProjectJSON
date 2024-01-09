from django.shortcuts import render
from django.http import JsonResponse
import json

def get_data(request):
    with open('data.json') as f:
        data = json.load(f)

    return render(request, 'index.html', {'data': data})