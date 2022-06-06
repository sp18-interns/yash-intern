from django.shortcuts import render,redirect
from .models import Meetup, Participant
from .forms import RegistrationForm
# Create your views here.

def index(request):
    meetups= Meetup.objects.all()  # This meetups variable of type list containing dictionary items is simulating dynamic data that
    # we will be using later.
    return render(request,"meetups/index.html",{'meetup':meetups})

def meetup_details(request,meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form= RegistrationForm()
        else:
            registration_form= RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email= registration_form.cleaned_data
                participants, was_created= Participant.objects.get_or_create(email=user_email)
                selected_meetup.participant.add(participants)
                return redirect('confirm-registration',meetup_slug=meetup_slug)

        return render(request,
                      'meetups/meetup_details.html',
                      {'meetup_found': True,
                       'meetup': selected_meetup,
                       'form': registration_form})

    except Exception as exc:
        print(exc)
        return render(request,
                      'meetups/meetup_details.html',
                      {'meetup_found': False})

def confirm_registration(request, meetup_slug):
    meetup= Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html',{
        'organizer_email':meetup.organizer_email
    })