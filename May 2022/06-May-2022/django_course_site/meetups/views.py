from django.shortcuts import render

# Create your views here.

def index(request):
    meetups=[
        {'title':'A first meetup'},
        {'title':'A second meetup'}
    ] # This meetups variable of type list containing dictionary items is simulating dynamic data that
    # we will be using later.
    return render(request,"meetups/index.html",{'meetups':meetups})