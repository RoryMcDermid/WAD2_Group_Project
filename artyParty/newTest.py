import os
import importlib
from django.urls import reverse
from django.test import TestCase

class ProjectStructureTests(TestCase):

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.arty_app_dir = os.path.join(self.project_base_dir, 'artyParty')


    def test_project_created(self):
        """
        Tests whether the wad_2_team_project configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'wad_2_team_project'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'wad_2_team_project', 'urls.py'))
