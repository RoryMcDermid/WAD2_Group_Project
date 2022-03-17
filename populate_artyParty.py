import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_2_team_project.settings')

import django
django.setup()
from artyParty.models import User, Gallery, Piece, Review


def populate():

    hunterian_pieces = [
        {'image': 'mona-lisa.jpeg',
         'piece_id': 11,
         'gallery_id': 1,
         'piece_name': 'Mona Lisa',
         'piece_category': 'Renaissance',
         'user_id': 2563582
         },
        {'image': 'cafe-terrace-at-night.jpg',
         'piece_id': 12,
         'gallery_id': 1,
         'piece_name': 'Cafe Terrace at Night',
         'piece_category': 'Post-Impressionism',
         'user_id': 2563582
         }
    ]

    goma_pieces = [
        {'image': 'nighthawks.jpeg',
         'piece_id': 21,
         'gallery_id': 2,
         'piece_name': 'Nighthawks',
         'piece_category': 'Modernism',
         'user_id': 2594321
         },
        {'image': 'the-persistence-of-memory.jpeg',
         'piece_id': 22,
         'gallery_id': 2,
         'piece_name': 'The Persistence of Memory',
         'piece_category': 'Surrealism',
         'user_id': 2594321
         },
        {'image': 'the-kiss',
         'piece_id': 23,
         'gallery_id': 2,
         'piece_name': 'The Kiss',
         'piece_category': 'Art Nouveau',
         'user_id': 2594321
         }
    ]

    kelvingrove_pieces = [
        {'image': 'lady-with-ermine.jpeg',
         'piece_id': 31,
         'gallery_id': 3,
         'piece_name': 'Lady with an Ermine',
         'piece_category': 'High Renaissance',
         'user_id': 3678912
         },
        {'image': 'girl-with-pearl.jpeg',
         'piece_id': 32,
         'gallery_id': 3,
         'piece_name': 'Girl with a Pearl Earring',
         'piece_category': 'Dutch Golden Age',
         'user_id': 3678912
         }
     ]

    galls = {}
