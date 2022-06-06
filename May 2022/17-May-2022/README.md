# Date 17-May-2022

## First Half

- 🔄Python Django- The Practical Guide : In Progress

### Videos

- ✅16 Optional Django Summary and Quick Introduction: Completed
  - ✅029 Polishing Organizer Email: Completed
  - ✅030 Optimizing URLs: Completed
  - ✅031 Wrap Up: Completed

### Assignment

- Added the links for contacting the organizer in both meetup-details page and confirmation-page.

```
 The link will open mail client to send a mail to the organizer of a specific meetup. Added changes to urls.py by incuding slug converter to provide the appropriate meetup slug in the parameters of path function and using this slug as keyword argument while calling redirect method in views.py.
```

```
Also added changes to definition of confirm_registration view function to accept specific meetup slug as keyword arguments which will be used to get a meetup object and this meetup object's organizer_email attribute is used as value for a key in the dictionary argument of render function. This key is used in the template mentioned in the render function using interpolation to provide the link for href attribute of HTML.
```

- Optimized the URLs using RedirectView class from django.views.generic.base module in our project's urls.py file and also made respective changes to our app's urls.py file by removing repetitive path.

### Doubts

- None

### Links Read

- None

## Second Half

- 🔄 Python Django- The Practical Guide: In Progress

### Videos

- ✅02 Course Setup: Completed
  - ✅001 to 008: Completed
- ✅03 URLs & Views: Completed
  - ✅001 to 013: Completed

### Assignment

- Watched and understood the videos.
- Created a new virtual environment and started practicing in a new project named 'monthly_challenges'.
- Created new URLs and views. Learnt about the reverse function which was not mentioned earlier in the summary section.
- Earlier, I used the name value(used to retrieve url details) from urls.py as first argument to redirect function(which is imported from django.shortcuts), here I passed name as argument of reverse function(which is imported from django.urls).

### Doubts

- Created new virtual environment to start new project. Had to pip install django again. Do we need to install django for every project again and again? Won't it take too much disk space eventually?

## Links Read

- [Cannot be loaded because running scripts is disabled on this system](https://stackoverflow.com/questions/67150436/cannot-be-loaded-because-running-scripts-is-disabled-on-this-system-for-more-in)
