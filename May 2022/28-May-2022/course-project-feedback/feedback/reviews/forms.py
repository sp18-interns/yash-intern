from django import forms

class ReviewForm(forms.Form):
    user_name= forms.CharField(label= "Your name", required= True, max_length= 100, error_messages={
        "required": "Your name must not be empty!",
        "max_length": "Please enter a shorter name"
    })