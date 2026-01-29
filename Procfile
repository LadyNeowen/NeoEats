# Run migrations automatically on deploy (prevents missing tables)
release: python manage.py migrate

# Start production server
web: gunicorn neoeats_project.wsgi
