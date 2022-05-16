from django.urls import path
from . import views
urlpatterns =[
    path('meetups/',views.index),# our-domain.com/meetups Adding / is good convention#
    path('meetups/success',views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>',views.meetup_details, name='meetup-detail'), # our-domain.com/meetups/<dynamic-path-segment>
]                                                           # slug: is a slug converter