import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_2_team_project.settings')

import django
django.setup()
from artyParty.models import User, Gallery, Piece, Review


def populate():

    hunterian_pieces = [
        {}
    ]