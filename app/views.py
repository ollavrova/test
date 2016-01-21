import random
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from pyshorteners import Shortener
from app.models import Shorted
from app.forms import UrlInputForm
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    form = UrlInputForm()
    if request.method == 'POST':
        form = UrlInputForm(request.POST)
        if form.is_valid():
            url = request.POST.get('url')
            shortener = Shortener('TinyurlShortener')
            short = {
                'long_url': url[7:],  # exclude 'http://' from url string
                'short_url': shortener.short(url)[19:],  # exclude 'http://tinyurl.com/
                'user': random.choice(User.objects.all())
            }
            print short
            try:
                shorted = Shorted.objects.get(long_url='http://'+short['long_url'])
            except ObjectDoesNotExist:
                shorted = Shorted.objects.create(**short)
            return HttpResponseRedirect('/links/'+str(shorted.id))

    return render(request, 'app/index.html', {'form': form})


def links(request, pk):
    if not id:
        raise Http404
    shorted = Shorted.objects.get(id=pk)

    return render(request, 'app/shorted.html', {'shorted': shorted})


def info(request, link):
    if not link:
        raise Http404
    elif link[0] == '!':
        link = link[1:]
    shorted = Shorted.objects.get(short_url=link)
    return render(request, 'app/info.html', {'shorted': shorted})

