import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_2_team_project.settings')
import django

django.setup()
from artyParty.models import User, Gallery, Piece, Review


def populate():
    mona_lisa_revs = [
        {'review_id': 1110,
         'piece_id': 110,
         'rating': 8.5,
         'user_id': 3678912,
         'review': 'Very good. I like.'}
    ]

    cafe_terr_night_revs = [
        {'review_id': 1210,
         'piece_id': 1200,
         'rating': 10,
         'user_id': 3678912,
         'review': 'OOOOOOO pretty'}
    ]

    hunterian_pieces = [
        {'piece_img': 'mona-lisa.jpeg',
         'piece_id': 1100,
         'gallery_id': 1,
         'piece_name': 'Mona Lisa',
         'author': 'Leonardo Da Vinci',
         'period': 'Renaissance',
         'user_id': 2563582,
         'reviews': mona_lisa_revs
         },
        {'piece_img': 'cafe-terrace-at-night.jpg',
         'piece_id': 1200,
         'gallery_id': 1,
         'piece_name': 'Café Terrace at Night',
         'author': 'Vincent van Gogh',
         'period': 'Post-Impressionism',
         'user_id': 2563582,
         'reviews': cafe_terr_night_revs
         }
    ]

    nighthawks_revs = [
        {'review_id': 2110,
         'piece_id': 2100,
         'rating': 6,
         'user_id': 3678912,
         'review': 'Nice colour scheme, lacks emotion.'}
    ]
    pers_of_mem_revs = [
        {'review_id': 2210,
         'piece_id': 2200,
         'rating': 3,
         'user_id': 2563582,
         'review': 'Too abstract and boring for me :/'}
    ]

    kiss_revs = [
        {'review_id': 2310,
         'piece_id': 2300,
         'rating': 10,
         'user_id': 2594321,
         'review': 'Absolute fav of all time.'}
    ]

    goma_pieces = [
        {'piece_img': 'nighthawks.jpeg',
         'piece_id': 2100,
         'gallery_id': 2,
         'piece_name': 'Nighthawks',
         'author': 'Edward Hopper',
         'period': 'Modernism',
         'user_id': 2594321,
         'reviews': nighthawks_revs
         },
        {'piece_img': 'the-persistence-of-memory.jpeg',
         'piece_id': 2200,
         'gallery_id': 2,
         'piece_name': 'The Persistence of Memory',
         'author': 'Salvador Dalí',
         'period': 'Surrealism',
         'user_id': 2594321,
         'reviews': pers_of_mem_revs
         },
        {'piece_img': 'the-kiss',
         'piece_id': 2300,
         'gallery_id': 2,
         'piece_name': 'The Kiss',
         'author': 'Gustav Klimt',
         'period': 'Art Nouveau',
         'user_id': 2594321,
         'reviews': kiss_revs
         }
    ]

    lady_with_ermine_revs = [
        {'review_id': 3110,
         'piece_id': 3100,
         'rating': 8,
         'user_id': 2594321,
         'review': 'Her left eye looks weird, everything else is good tho'}
    ]
    girl_with_pearl_revs = [
        {'review_id': 3210,
         'piece_id': 3200,
         'rating': 10,
         'user_id': 2563582,
         'review': 'Now THIS is epic. Masterpiece.'}
    ]

    kelvingrove_pieces = [
        {'piece_img': 'lady-with-ermine.jpeg',
         'piece_id': 3100,
         'gallery_id': 3,
         'piece_name': 'Lady with an Ermine',
         'author': 'Leonardo Da Vinci',
         'period': 'High Renaissance',
         'user_id': 3678912,
         'reviews': lady_with_ermine_revs
         },
        {'piece_img': 'girl-with-pearl.jpeg',
         'piece_id': 3200,
         'gallery_id': 3,
         'piece_name': 'Girl with a Pearl Earring',
         'author': 'Johannes Vermeer',
         'period': 'Dutch Golden Age',
         'user_id': 3678912,
         'reviews': girl_with_pearl_revs
         }
    ]

    galls = {'The Hunterian': {'gallery_id': 1,
                               'user_id': 2563582,
                               'gallery_description': 'Impressive display of the finest Scottish art pieces, '
                                                      'situated at the University of Glasgow',
                               'pieces': hunterian_pieces},

             'Gallery of Modern Art': {'gallery_id': 2,
                                       'user_id': 2594321,
                                       'gallery_description': 'Located at the heart of Glasgow, the Gallery of '
                                                              'Modern Art houses immersive exhibits for enthusiasts '
                                                              'of modern art and anyone alike.',
                                       'pieces': goma_pieces},

             'Kelvingrove Art Gallery': {'gallery_id': 3,
                                         'user_id': 3678912,
                                         'gallery_description': 'The Kelvingrove Art Gallery & Museum is home to a'
                                                                ' wide range of pieces from a variety of periods that '
                                                                'anyone can admire.',
                                         'pieces': kelvingrove_pieces}}

    users = [
        {'user_id': 2563582, 'user_name': 'jnpawlowska123', 'user_type': 'superuser'},
        {'user_id': 2594321, 'user_name': 'leodastinki', 'user_type': 'superuser'},
        {'user_id': 3678912, 'user_name': 'vinvangoth', 'user_type': 'superuser'}
    ]

    # Goes through galls dictionary and adds each gallery
    # Then adds all the pieces in the gallery
    # and all the reviews for the pieces
    for gal, gal_data in galls.items():
        g = add_galls(gal, gal_data['gallery_id'], gal_data['user_id'], gal_data['gallery_description'])
        for p in gal_data['pieces']:
            piece = add_piece(g['gallery_id'], p['piece_img'], p['piece_id'], p['piece_name'], p['author'],
                              p['period'], p['user_id'])
            for r in piece['reviews']:
                add_review(r['review_id'], piece['piece_id'], r['rating'], r['user_id'], r['review'])

    # Print out the galleries we have added.
    for g in Gallery.objects.all():
        for p in Piece.objects.filter(gallery=g):
            print(f'- {g}: {p}')

    for user in users:
        add_user(user['user_id'], user['user_name'], user['user_type'] )


def add_piece(gallery_id, piece_img, piece_id, piece_name, author, period, user_id):
    p = Piece.objects.get_or_create(piece_img=piece_img, piece_id=piece_id, gallery_id=gallery_id,
                                    piece_name=piece_name, author=author, period=period, user_id=user_id)
    p.save()
    return p


def add_galls(gallery_name, gallery_id, user_id, gallery_description):
    g = Gallery.objects.get_or_create(gallery_name=gallery_name, gallery_id=gallery_id, user_id=user_id,
                                      gallery_description=gallery_description)
    g.save()
    return g


def add_review(review_id, piece_id, rating, user_id, review):
    r = Review.objects.get_or_create(review_id=review_id, piece_id=piece_id, rating=rating,
                                     user_id=user_id, review=review)
    r.save()
    return r


def add_user(user_id, user_name, user_type):
    u = User.objects.get_or_create(user_id=user_id, user_name=user_name, user_type=user_type)
    u.save()
    return u


# Start execution
if __name__ == '__main__':
    print('Starting ArtyParty population script...')
    populate()
