from django.shortcuts import render
import requests
import time
from rest_framework import status
from rest_framework.response import Response
from django.utils.safestring import SafeString

def index(request):
    return render(request, 'index.html')


def api(request):
    import os
    username = 'AntonBalmakov'
    token = os.environ.get("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")
    r = requests.get("https://api.github.com",auth=(username, token))
    r = r.json()
    print(r)
    return render(request, 'test.html', {'r': SafeString(r)})