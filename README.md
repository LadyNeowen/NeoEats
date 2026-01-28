# NeoEats

## NeoEats Restaurant Website

NeoEats is a modern, fully responsive restaurant website built with Django, featuring a custom CMS, an image gallery powered by Cloudinary, and deployment through Heroku.

It allows the restaurant owner to manage menu items, gallery images, “About” text, and booking information through Django Admin.

The site is designed to work seamlessly on desktop, tablet, and mobile devices.

<br>

# How the Site Looks on Different Devices
![Responsiveness](./README_images/Responsiveness.jpg)


# How It Works
## NeoEats is a content-managed restaurant website consisting of:

### About Page 
![About NeoEats](./README_images/About.jpg) 
![Working With Our Farmers](./README_images/Farmers.jpg)

### Gallery 
![Gallery](./README_images/Gallery.jpg)

### Menu Page 
![Responsive Menu](./README_images/Responsive_menu.jpg)

### Booking Page 
![Book a Table](./README_images/Book_table.jpg)




Editable title + text.

Dynamically generated from Django models—add dishes in the admin panel.

Editable title + text.

Uses Cloudinary to store and serve gallery images with fast CDN delivery.

A simple reservation form styled to match the site’s aesthetic.

Home Page

Hero image, introduction text, and navigation links.

All content is editable through Django Admin, without ever touching the codebase.

<br>

# Features
## Core Features

Fully responsive layout

Custom Django CMS (About, Menu Items, Gallery, Collaboration Page)

Gallery with Cloudinary image hosting

Booking page with form

Accessible navigation and clear design

Deployed on Heroku

Static files served via Whitenoise

Media files through Cloudinary

Admin Features

Upload and manage images

Add/edit/delete menu items

Edit About page content

Edit collaboration/farmers page

Simple and clean admin UI

Newsletter signup

<br>

# Future Features

Booking email confirmations

Multi-category menu filtering

Customer reviews page

Add alt-text fields to gallery images

<br>

# Testing

## All templates tested across Chrome, Edge, Safari, and mobile devices

## Manual testing of:

Image uploads

Form inputs

Navigation

Page responsiveness

Django server tested locally with DEBUG on and off

Verified static & media file behavior in production

Cloudinary URL reliability confirmed

## Automated testing 
Was implemented across multiple apps using Django’s built-in TestCase.

All tests are stored inside each app’s tests/ directory following Django’s recommended structure.

Each app contains a dedicated test suite:

app/tests/
* test_models.py
* test_views.py
* test_urls.py
* test_templates.py
* test_forms.py        (Booking app only)
* test_admin.py
* test_apps.py
* __init__.py

## What Was Tested:

### Core App

* View renders correct template.
* URL resolves to correct view.
* Template contains expected hero banner text.
* App configuration loads correctly.

### Menu App

* MenuItem model: string method & category choices.
* Menu view: context groups dishes by category.
* URL resolution.
* Admin registration.
* Template displays menu items correctly.
* AppConfig.

### About App

* Models (AboutPage, GalleryImage, CollaborationPage).
* Views: about, gallery, collaboration pages.
* URL patterns.
* Templates: content rendered correctly.
* Admin registration.

### Booking App

* Models: booking + newsletter.
* Forms: validation and custom clean logic.
* Views: booking logic, newsletter logic.
* URLs.
* Templates: form fields and errors.
* Admin registration.

### Running the Tests

python manage.py test appname.tests



<br>

## Solved Bugs

Heroku staticfiles 500 error fixed by:

Adding STATIC_ROOT

Removing broken .venv/ folder from repo

Allowing Heroku to run collectstatic normally

Cloudinary images not loading:

Fixed malformed CLOUDINARY_URL config

Images missing due to local static folder conflict — resolved by cleaning static directory

VSCode virtual environment accidentally committed — fixed with .gitignore and repo cleanup

Deleted and recreated deployments after debugging environment conflicts

<br>

# Remaining Bugs

None currently known.

<br>

# Validator Testing

Python code validated using PEP8 tools

HTML validated through W3C validator

No major issues encountered

<br>

# Heroku Deployment Steps

Create a new Heroku app

Add buildpack: heroku/python

Add required Config Vars:

DATABASE_URL

CLOUDINARY_URL

SECRET_KEY

Ensure the .venv directory is not in Git

Push to Heroku using:

git push heroku main

Live site deploys at:
https://neoeats-62e4965fe040.herokuapp.com/

<br>

# Credits

Cloudinary for image hosting

Heroku for deployment

Django documentation for model/template references

Bootstrap for styling layout

My mentor for guidance

ChatGPT for debugging and explanations along the way

ChatGPT for docstring documentation

ami.responsive for device preview screenshot

# Inspiration:
* LMA Content
* https://restaurant--booking-465b6b7fd829.herokuapp.com/
* https://github.com/DiarmuidHenry/Restaurant-Booking
* https://www.youtube.com/watch?v=DIFaOkxy6TE (User Registration and login)

## Models
* https://www.freecodecamp.org/news/how-to-create-models-in-your-django-project/?utm_source=chatgpt.com
* https://docs.djangoproject.com/en/5.2/topics/db/models/?utm_source=chatgpt.com
* https://www.digitalocean.com/community/tutorials/how-to-create-django-models?utm_source=chatgpt.com

## Testing
* https://docs.djangoproject.com/en/5.2/topics/testing/overview/?utm_source=chatgpt.com
* https://realpython.com/pytest-python-testing/ (And many other areas, I signed up with them to get lessons. )



