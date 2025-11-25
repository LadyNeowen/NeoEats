'''
Environment configuration for the NeoEats project.

Sets required environment variables for development.
'''

import os

# Enable Django debug mode locally (Heroku ignores this file)
os.environ.setdefault('DEBUG', 'True')

# Local Secret Key (ONLY used for local development)
os.environ.setdefault(
    'SECRET_KEY',
    's_s%80g3@-y+!62@g1u@c!=nr&fkk-p04=px0s_8*u6!x=$ca+',
)

# Local database (Neon)
os.environ.setdefault(
    'DATABASE_URL',
    (
        'postgresql://neondb_owner:'
        'npg_fUAgP8EC1wZe@ep-withered-cell-ag25se60.'
        'c-2.eu-central-1.aws.neon.tech/boss_lunar_outer_601119'
    ),
)

# Cloudinary credentials (local development)
os.environ.setdefault('CLOUDINARY_CLOUD_NAME', 'djprwhser')
os.environ.setdefault('CLOUDINARY_API_KEY', '146627353726298')
os.environ.setdefault('CLOUDINARY_API_SECRET', 'jsfygJjUk-DIz6Ko3s5QAZ7QOu8')