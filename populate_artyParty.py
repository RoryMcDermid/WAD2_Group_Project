import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_2_team_project.settings')
import django

django.setup()
from artyParty.models import Gallery, Piece, Review, UserProfile
from django.contrib.auth.models import User




def populate():
    mona_lisa_revs = [
        {'review_id': 1110,
        'piece_id': 110,
        'rating': 8.5,
        'userID': 2563582,
        'review': 'Very good. I like.'}
    ]

    cafe_terr_night_revs = [
        {'review_id': 1210,
        'piece_id': 1200,
        'rating': 10,
        'userID': 2563582,
        'review': 'OOOOOOO pretty'}
    ]

    hunterian_pieces = [
        {'piece_img': 'mona-lisa.jpeg',
        'piece_id': 1100,
        'piece_name': 'Mona Lisa',
        'author': 'Leonardo Da Vinci',
        'period': 'Renaissance',
        'userID': 2563582,
        'reviews': mona_lisa_revs
        },
        {'piece_img': 'cafe-terrace-at-night.jpg',
        'piece_id': 1200,
        'piece_name': 'Café Terrace at Night',
        'author': 'Vincent van Gogh',
        'period': 'Post-Impressionism',
        'userID': 2563582,
        'reviews': cafe_terr_night_revs
        }
    ]

    nighthawks_revs = [
        {'review_id': 2110,
        'piece_id': 2100,
        'rating': 6,
        'userID': 2563582,
        'review': 'Nice colour scheme, lacks emotion.'}
    ]
    pers_of_mem_revs = [
        {'review_id': 2210,
        'piece_id': 2200,
        'rating': 3,
        'userID': 2563582,
        'review': 'Too abstract and boring for me :/'}
    ]

    kiss_revs = [
        {'review_id': 2310,
        'piece_id': 2300,
        'rating': 10,
        'userID': 2563582,
        'review': 'Absolute fav of all time.'}
    ]

    goma_pieces = [
        {'piece_img': 'nighthawks.jpg',
        'piece_id': 2100,
        'piece_name': 'Nighthawks',
        'author': 'Edward Hopper',
        'period': 'Modernism',
        'userID': 2563582,
        'reviews': nighthawks_revs
        },
        {'piece_img': 'the-persistence-of-memory.jpg',
        'piece_id': 2200,
        'piece_name': 'The Persistence of Memory',
        'author': 'Salvador Dalí',
        'period': 'Surrealism',
        'userID': 2563582,
        'reviews': pers_of_mem_revs
        },
        {'piece_img': 'the-kiss.jpg',
        'piece_id': 2300,
        'piece_name': 'The Kiss',
        'author': 'Gustav Klimt',
        'period': 'Art Nouveau',
        'userID': 2563582,
        'reviews': kiss_revs
        }
    ]

    lady_with_ermine_revs = [
        {'review_id': 3110,
        'piece_id': 3100,
        'rating': 8,
        'userID': 2563582,
        'review': 'Her left eye looks weird, everything else is good tho'}
    ]
    girl_with_pearl_revs = [
        {'review_id': 3210,
        'piece_id': 3200,
        'rating': 10,
        'userID': 2563582,
        'review': 'Now THIS is epic. Masterpiece.'}
    ]

    kelvingrove_pieces = [
        {'piece_img': 'lady-with-ermine.jpg',
        'piece_id': 3100,
        'piece_name': 'Lady with an Ermine',
        'author': 'Leonardo Da Vinci',
        'period': 'High Renaissance',
        'userID': 2563582,
        'reviews': lady_with_ermine_revs
        },
        {'piece_img': 'girl-with-pearl.jpg',
        'piece_id': 3200,
        'piece_name': 'Girl with a Pearl Earring',
        'author': 'Johannes Vermeer',
        'period': 'Dutch Golden Age',
        'userID': 2563582,
        'reviews': girl_with_pearl_revs
        }
    ]

    galls = {'The Hunterian': {'gallery_id': 1,
                                'userID': 2563582,
                                'gallery_description': 'Impressive display of the finest Scottish art pieces, '
                                                        'situated at the University of Glasgow',
                                'pieces': hunterian_pieces,
                                'gallery_img': 'The-Hunterian-Museum.jpg'},

                'Gallery of Modern Art': {'gallery_id': 2,
                                            'userID': 2563582,
                                            'gallery_description': 'Located at the heart of Glasgow, the Gallery of '
                                                                    'Modern Art houses immersive exhibits for enthusiasts '
                                                                    'of modern art and anyone alike.',
                                            'pieces': goma_pieces,
                                            'gallery_img': 'MODERN.jpg'},

                'Kelvingrove Art Gallery': {'gallery_id': 3,
                                            'userID': 2563582,
                                            'gallery_description': 'The Kelvingrove Art Gallery & Museum is home to a'
                                                                ' wide range of pieces from a variety of periods that '
                                                                'anyone can admire.',
                                            'pieces': kelvingrove_pieces,
                                            'gallery_img': 'k2.jpg'}}

    user_dict = [{'user_id': 2563582, 'user_name': 'jnpawlowska123', 'user_type': True},
                {'user_id': 2594321, 'user_name': 'leodastinki', 'user_type': True},
                {'user_id': 3678912, 'user_name': 'vinvangoth', 'user_type': True}]


    print('Adding users...')

    for user in user_dict:
        add_user_supertype(user['user_id'], user['user_name'], user['user_type'])

    users = User.objects.all()
    for user in users:
        user_id = user.id
        add_user(user, user_id)

    print("Users done")
    # Goes through galls dictionary and adds each gallery
    # Then adds all the pieces in the gallery
    # and all the reviews for the pieces
    for gal, gal_data in galls.items():
        user = UserProfile.objects.get(user_id=gal_data['userID']).user
        print(f" Adding {gal}")
        g = add_galls(gal, gal_data['gallery_id'], user, gal_data['gallery_description'], gal_data['gallery_img'])
        for p in gal_data['pieces']:
            add_piece(g, p['piece_img'], p['piece_id'], p['piece_name'], p['author'],
                        p['period'], UserProfile.objects.get(user_id=p['userID']).user)
            for r in p['reviews']:
                add_review(r['review_id'], Piece.objects.get(piece_id=p['piece_id']), r['rating'], UserProfile.objects.get(user_id=r['userID']).user, r['review'])

    # Print out the galleries we have added.
    for g in Gallery.objects.all():
        for p in Piece.objects.filter(gallery_id=g):
            print(f'- {g.gallery_name}: {p.piece_name}')


def add_user(user, userID):
    u = UserProfile.objects.get_or_create(user=user, userID=userID)[0]
    u.save()
    return u


def add_piece(gallery_id, piece_img, piece_id, piece_name, author, period, user):
    p = Piece.objects.get_or_create(piece_img=piece_img, piece_id=piece_id, gallery_id=gallery_id,
                                    piece_name=piece_name, author=author, period=period, userID=user)[0]
    p.save()
    return p


def add_galls(gallery_name, gallery_id, user, gallery_description, img):
    g = Gallery.objects.get_or_create(gallery_name=gallery_name, gallery_id=gallery_id,
                                        gallery_description=gallery_description, userID=user, gallery_img=img)[0]

    g.save()
    return g


def add_review(review_id, piece_id, rating, userID, review):
    r = Review.objects.get_or_create(review_id=review_id, piece_id=piece_id, rating=rating,
                                        userID=userID, review=review)[0]
    r.save()
    return r


def add_user_supertype(user_id, user_name, user_type):
    u = User.objects.get_or_create(id=user_id, username=user_name, is_superuser=user_type)
    return u


# Start execution
if __name__ == '__main__':
    print('Starting ArtyParty population script...')
    populate()
