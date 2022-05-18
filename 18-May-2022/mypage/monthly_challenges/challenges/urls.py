from django.urls import path
from . import views

# handler404 = 'challenges.views.custom_page_not_found_view'
urlpatterns= [
    path('',views.index, name='index'),
    path('<int:month>',views.monthly_challenge_by_number),
    path('<str:month>',views.monthly_challenge,name='month-challenge')
]