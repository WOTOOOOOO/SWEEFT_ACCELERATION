import random
import string
import validators
from django.core import serializers

from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import *
from .models import UrlData

# I was using postman to test my api, so unfortunately I was forced to disable csrf tokens, I wrote a script
# to automatically set the token in the header, but it simply wouldn't work.

# locahost:8000
# URL shortening
@csrf_exempt
def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            if not validators.url(url) or len(url) > 250:
                return HttpResponse("Your URL is invalid")
            slug = ''.join(random.choice(string.ascii_letters) for x in range(15))
            new_url = UrlData(url=url, slug=slug, count=0)
            new_url.save()
            return HttpResponse(f"Your shortened URL is http://localhost:8000/u/{slug}")
        else:
            print(form.errors)
            return HttpResponse("An error occurred input you URL please")
    else:
        return HttpResponse("Internal error")

# localhost:8000/p/
# Premium URL shortening
@csrf_exempt
def premiumUrlShort(request):
    if request.method == 'POST':
        form = CustomUrl(request.POST)
        if form.is_valid():
            url = form.cleaned_data["url"]
            if not validators.url(url) or len(url) > 250:
                return HttpResponse("Your URL is invalid")
            customName = form.cleaned_data["name"]
            if UrlData.objects.filter(slug = customName).exists():
                return HttpResponse("A Url with this name already exists, input a different custom name")
            new_url = UrlData(url=url, slug=customName, count=0)
            new_url.save()
            return HttpResponse(f"Your shortened URL is http://localhost:8000/u/{customName}")
        else:
            print(form.errors)
            return HttpResponse("An error occurred input your URL please")
    else:
        return HttpResponse("Internal error")

# localhost:8000/u/{slug}/
# Redirect to the real URL
@csrf_exempt
def urlRedirect(request, slugs):
    data = UrlData.objects.get(slug=slugs)
    data.count = data.count + 1
    data.save()
    return redirect(data.url)

# localhost:8000/a/
# Get the data of all URLs
@csrf_exempt
def allUrls(request):
    data = UrlData.objects.all()
    data_json = serializers.serialize('json', data)
    return HttpResponse(data_json, content_type='application/json')

# localhost:8000/d/
# Delete a URLs
@csrf_exempt
def deleteUrl(request):
    if request.method == 'POST':
        form = Slugs(request.POST)
        if form.is_valid():
            slugs = form.cleaned_data["slug"]
            data = UrlData.objects.get(slug=slugs)
            data.delete()
            return HttpResponse(f"Succesfully deleted https://localhost:8000/u/{slugs}")
        else:
            print(form.errors)
            return HttpResponse("An error occurred please input your slug again")
    else:
        return HttpResponse("Internal error")


# localhost:8000/data/
# Get the data of a specific URLs
@csrf_exempt
def urlData(request):
    if request.method == 'POST':
        form = Slugs(request.POST)
        if form.is_valid():
            slugs = form.cleaned_data["slug"]
            print(slugs)
            data = UrlData.objects.get(slug=slugs)
            data_json = serializers.serialize('json', [data])
            return HttpResponse(data_json, content_type='application/json')
        else:
            print(form.errors)
            return HttpResponse("An error occurred please input your slug again")
    else:
        return HttpResponse("Internal error")
