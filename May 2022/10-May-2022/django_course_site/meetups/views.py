from django.shortcuts import render

# Create your views here.

def index(request):
    meetups=[
        {   'title':'A first meetup',
            'location': 'Pune',
            'slug': 'a-first-meetup'},

        {   'title':'A second meetup',
            'location': 'Mumbai',
            'slug': 'a-second-meetup'}
    ] # This meetups variable of type list containing dictionary items is simulating dynamic data that
    # we will be using later.
    return render(request,"meetups/index.html",{'show_meetups':True,'meetup':meetups})

def meetup_details(request,meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title':'A first meetup',
        'description': 'This is the first meetup!'
    }
    return render(request,
                  'meetups/meetup_details.html',
                  {'meetup_title': selected_meetup['title'],
                   'meetup_description': selected_meetup['description']})