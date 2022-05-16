# Date 16-May-2022

## First Half

- 🔄Python Django- The Practical Guide : In Progress

### Videos

- 🔄16 Optional Django Summary and Quick Introduction: In Progress
  - ✅019 Adding Image Upload: Completed
  - ✅020 Serving and Displaying Images: Completed
  - ✅021 Configuring the Admin Area: Completed
  - ✅022 Setting One-to-Many Relations: Completed
  - ✅023 Setting Many-to-Many Relations: Completed

### Assignment

- Revised by watching previous videos to recap what I learned.
- Watched and understood the videos. Also,practiced in the attached django_course_site project.
- Added a new Participant class to my model which was used to set a many to many relations with Meetup Class(using models.ManytoManyField()). Also viewed the behind the scene creation by Django of an additional table in DB Viewer with meetup_id and particiant_id as columns of that table

### Doubts

- None

### Links Read

- [Storing image in database](https://www.quora.com/What-is-the-best-approach-to-store-image-into-SQLite)

## Second Half

- 🔄 Python Django- The Practical Guide: In Progress

### Videos

- ✅024 More Meetup Fields and Outputting Related Data: Completed
- ✅025 Creating a Model Form: Completed
- ✅026 Handling Form Submission: Completed
- ✅027 More on Form Submission & Validation: Completed
- ✅028 From ModelForm to Form: Completed

### Assignment

- Added small changes to admin.py and views.py to add date,organizer_email and location data for meetups.
- Learnt about creating a form model so that visitors of the site can input data of a specific type by adding a forms.py file where we create a Registration Form class inheriting from ModelForm class.
- Learnt about handling form submission by adding conditions for GET and POST requests in views.py file.
- Learnt to create a new URL,view function and template to display registration confirmation of a participant of a meetup. Used the redirect method to redirect the visitor to a specific page. Learnt how Django automatically displays error messages and the invalid input after checking the validity condition.
- Learnt about using Form class instead of ModelForm class to create Registration Form class. Added conditions in views.py so that same email id can sign up for different meetup events.To enable that, we used cleaned_data attribute of Form class in place of save() method of ModelForm class.

### Doubts

- Got stuck in rendering confirmed registration page. Ultimately resolved as I called cleaned_data(dict attribute) as a method which was wrong as this dict object is not callable.

## Links Read

- [NULL object has no effect on ManytoManyField](https://blog.karatos.in/a?ID=229e9961-c065-490e-9635-4b259cfd34d9)
