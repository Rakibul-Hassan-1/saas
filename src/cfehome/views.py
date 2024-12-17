from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageVisit
# this_dir = pathlib.Path(__file__).resolve().parent
def home_view(request, *args, **kwargs): 
    return about_view(request, *args, **kwargs)

def about_view(request, *args, **kwargs):
    html_ = ""
    qs = PageVisit.objects.all()
    name = "Rakib"
    try:
        percent = ((qs.count()*100.0)/100)
    except:
        percent = 0
    my_title = {
        "myname" : name,
        "page_visits_count": qs.count(),
        "percent": percent,
    }
    html_ = "home.html"
    PageVisit.objects.create()
    return render(request, html_,my_title)

