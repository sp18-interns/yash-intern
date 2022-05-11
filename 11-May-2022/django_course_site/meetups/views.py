from django.shortcuts import render
from .models import Meetup
# Create your views here.

def index(request):
    meetups= Meetup.objects.all()  # This meetups variable of type list containing dictionary items is simulating dynamic data that
    # we will be using later.
    return render(request,"meetups/index.html",{'meetup':meetups})

def meetup_details(request,meetup_slug):
    try:
        selected_meetup= Meetup.objects.get(slug=meetup_slug)
        return render(request,
                      'meetups/meetup_details.html',
                      {'meetup_found': True,
                       'meetup_title': selected_meetup.title,
                       'meetup_description': selected_meetup.description})
    except Exception as exc:
        return render(request,
                      'meetups/meetup_details.html',
                      {'meetup_found': False})