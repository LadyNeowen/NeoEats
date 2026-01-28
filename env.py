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
    'i#p1_2pnt788#-$4blc_pfx07c$2+o$me^loh(@ma4$)oa*olm',
)

# Local database (Neon)

os.environ.setdefault(
    "CLOUDINARY_URL",
    "cloudinary://273141456562758:88Sjz0xznavx8PTOTD_GyG7vzvo@djprwhser"
)