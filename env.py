'''
Environment configuration for NeoEats project.

Sets required environment variables for development.
'''

import os

os.environ.setdefault(
    'DATABASE_URL',
    'postgresql://neondb_owner:npg_fUAgP8EC1wZe@ep-withered-cell-ag25se60.c-2.eu-central-1.aws.neon.tech/boss_lunar_outer_601119'
)
