import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad_2_team_project.settings')
import django
django.setup()
from artyParty.models import User


def populate():
    users = [{'user_id': 2563582, 'user_name': 'jnpawlowska123', 'user_type': True},
             {'user_id': 2594321, 'user_name': 'leodastinki', 'user_type': True},
             {'user_id': 3678912, 'user_name': 'vinvangoth', 'user_type': True}]

    for user in users:
        add_user(user['user_id'], user['user_name'], user['user_type'])


def add_user(user_id, user_name, user_type):
    u = User.objects.get_or_create(id=user_id, username=user_name, is_superuser=user_type)
    return u


# Start execution
if __name__ == '__main__':
    print('Starting ArtyParty User population script...')
    populate()
