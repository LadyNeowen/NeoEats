'''
Environment configuration for NeoEats project.

Sets required environment variables for development.
'''

import os

os.environ.setdefault(
    'DATABASE_URL',
    'postgresql://neondb_owner:npg_fUAgP8EC1wZe@ep-withered-cell-ag25se60.c-2.eu-central-1.aws.neon.tech/boss_lunar_outer_601119'
)

# os.environ.setdefault(
#     'CLOUDINARY_URL',
#     'cloudinary://146627353726298:jsfygJjUk-DIz6Ko3s5QAZ7QOu8@djprwhser?secure=true'
# )

os.environ.setdefault("CLOUDINARY_CLOUD_NAME", "djprwhser")
os.environ.setdefault("CLOUDINARY_API_KEY", "146627353726298")
os.environ.setdefault("CLOUDINARY_API_SECRET", "jsfygJjUk-DIz6Ko3s5QAZ7QOu8")
