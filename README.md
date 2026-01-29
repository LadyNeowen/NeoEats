# NeoEats

## NeoEats Restaurant Website

NeoEats is a modern, fully responsive restaurant website built with Django. It features a custom CMS, an image gallery powered by Cloudinary, and an online booking system. The project is deployed using Heroku.

The platform allows restaurant staff to manage menu items, gallery images, “About” content, and booking information through Django Admin.

The site is optimised for desktop, tablet, and mobile devices.

---

## Live Site

🔗 https://neoeats-62e4965fe040.herokuapp.com/

---

## Responsive Design

![Responsiveness](./README_images/Responsiveness.jpg)

---

## Pages & Functionality

### Home Page
* Hero banner
* Introduction text
* Navigation links

### About Page
![About NeoEats](./README_images/About.jpg)  
![Working With Our Farmers](./README_images/Farmers.jpg)

* Editable title and content
* Managed through Django Admin

### Gallery
![Gallery](./README_images/Gallery.jpg)

* Cloudinary-powered image hosting
* CDN delivery for performance

### Menu
![Responsive Menu](./README_images/Responsive_menu.jpg)

* Dynamically generated from database
* Categorised dishes
* Admin-managed

### Booking
![Book a Table](./README_images/Book_table.jpg)

* Secure booking form
* User authentication
* Newsletter signup

---

python manage.py runserver
## Features

### Core Features
* Fully responsive layout
* Custom Django CMS
* Cloudinary media storage
* Booking system
* Newsletter signup
* Secure authentication
* Accessible navigation

### Admin Features
* Image management
* Menu management
* Content editing
* Booking administration
* Clean admin interface

### Technical Features
* Django framework
* PostgreSQL database
* Whitenoise for static files
* Cloudinary for media
* Heroku deployment

---

## Future Enhancements
* Automated booking confirmation emails
* Advanced menu filtering
* Customer reviews
* Image alt-text support
* Analytics dashboard

---

## Testing

### Automated Testing

Each Django app follows a consistent testing structure:

```app_name/tests/
├── __init__.py
├── test_models.py
├── test_views.py
├── test_urls.py
├── test_templates.py
├── test_admin.py
├── test_apps.py
└── test_forms.py   (Booking app only)
```

---

### Test Coverage

#### Core App
* View rendering
* URL resolution
* Template content
* App configuration

#### Menu App
* Model validation
* Category grouping
* View context
* URL mapping
* Admin registration

#### About App
* Models
* Views
* URLs
* Templates
* Admin setup

#### Booking App
* Models
* Form validation
* Booking logic
* Newsletter logic
* View behaviour
* URL resolution

---

### Running Tests

**Test suite result: 45 tests across about, booking, core, and menu apps. All passing.**

### Manual Testing
* Cross-browser testing (Chrome, Edge, Safari)
* Mobile responsiveness
* Form validation
* Navigation flow
* Media uploads
* Production static/media handling

---

## Bug Fixes

### Resolved Issues
* Heroku staticfiles 500 error
* Cloudinary URL misconfiguration
* Static directory conflicts
* Accidental virtual environment commits
* Deployment environment inconsistencies

All known critical issues have been resolved.

---

## Known Issues

No known unresolved bugs at this time.

---

## Validation and formatting

* Python: PEP8 compliance
* HTML: W3C validation
* CSS: W3C validation
* black .
* flake8 .

No major validation errors detected.

---

## Deployment

* Database migrations run automatically via Procfile release phase.
* Prevents missing table errors on Heroku.

### Heroku Deployment Steps

1. Create a new Heroku app
2. Add Python buildpack
3. Configure environment variables:
   * DATABASE_URL
   * CLOUDINARY_URL
   * SECRET_KEY
4. Ensure .venv is excluded via .gitignore
5. Push to Heroku:
6. Run migrations and collectstatic

---

## Technologies Used
* Python
* Django
* PostgreSQL
* HTML5
* CSS3
* Bootstrap
* Cloudinary
* Heroku

---

## References

### Authentication & Permissions
* https://docs.djangoproject.com/en/6.0/topics/auth/
* https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Authentication

### Forms & Views
* https://docs.djangoproject.com/en/6.0/topics/forms/
* https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/#get-object-or-404

### Models
* https://docs.djangoproject.com/en/5.2/topics/db/models/
* https://www.digitalocean.com/community/tutorials/how-to-create-django-models

### Testing
* https://docs.djangoproject.com/en/5.2/topics/testing/overview/
* https://realpython.com/pytest-python-testing/


---

## Credits and Acknowledgements
* Cloudinary (image hosting)
* Heroku (deployment)
* Django Documentation
* Bootstrap
* ami.responsive
* Mentor support
* LMA Content
* https://unsplash.com/ (Images)
* https://restaurant--booking-465b6b7fd829.herokuapp.com/  
* https://github.com/DiarmuidHenry/Restaurant-Booking  
* https://www.youtube.com/watch?v=DIFaOkxy6TE

* ## ChatGPT
* Docstring documentations
* Debugging and assistance
* Swedish translation and explinations
* Structuring and folder build
* Test strategy guidance

---

