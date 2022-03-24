import os
import importlib
from django.urls import reverse
from django.test import TestCase
from django.conf import settings


# request factory

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}Arty Test Fail{os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"


class ProjectStructureTests(TestCase):
    """
    File structure tests
    """

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.arty_app_dir = os.path.join(self.project_base_dir, 'artyParty')

    def test_project_created(self):
        """
        Tests whether the wad_2_team_project configuration directory is present and correct.
        """
        directory_exists = os.path.isdir(os.path.join(self.project_base_dir, 'wad_2_team_project'))
        urls_module_exists = os.path.isfile(os.path.join(self.project_base_dir, 'wad_2_team_project', 'urls.py'))

        self.assertTrue(directory_exists,
                        f"{FAILURE_HEADER}No configuration directory{FAILURE_FOOTER}")
        self.assertTrue(urls_module_exists,
                        f"{FAILURE_HEADER}Your project's urls.py module does not exist. Did you use the startproject command?{FAILURE_FOOTER}")

    def test_arty_app_created(self):
        """
        Determines whether the app has been created.
        """
        directory_exists = os.path.isdir(self.arty_app_dir)
        is_python_package = os.path.isfile(os.path.join(self.arty_app_dir, '__init__.py'))
        views_module_exists = os.path.isfile(os.path.join(self.arty_app_dir, 'views.py'))

        self.assertTrue(directory_exists,
                        f"{FAILURE_HEADER}The arty app directory does not exist. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(is_python_package,
                        f"{FAILURE_HEADER}The arty directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")
        self.assertTrue(views_module_exists,
                        f"{FAILURE_HEADER}The arty directory is missing files. Did you use the startapp command?{FAILURE_FOOTER}")

    def test_arty_has_urls_module(self):
        """
        Did you create a separate urls.py module for arty?
        """
        module_exists = os.path.isfile(os.path.join(self.arty_app_dir, 'urls.py'))
        self.assertTrue(module_exists,
                        f"{FAILURE_HEADER}The arty app's urls.py module is missing. Read over the instructions carefully, and try again. You need TWO urls.py modules.{FAILURE_FOOTER}")

    def test_is_arty_app_configured(self):
        """
        Did you add the new arty app to your INSTALLED_APPS list?
        """
        is_app_configured = 'artyParty' in settings.INSTALLED_APPS

        self.assertTrue(is_app_configured,
                        f"{FAILURE_HEADER}The arty app is missing from your setting's INSTALLED_APPS list.{FAILURE_FOOTER}")


class IndexPageTests(TestCase):
    """
    Testing the basics of your index view and URL mapping.
    Also runs tests to check the response from the server.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

        self.project_urls_module = importlib.import_module('wad_2_team_project.urls')

    def test_project_mappings(self):
        """
        Are the two required URL mappings present and correct?
        One should be in the project's urls.py, the second in arty's urls.py.
        We have the 'index' view named twice -- it should resolve to '/arty/'.
        """
        index_mapping_exists = False

        # This is overridden. We need to manually check it exists.
        for mapping in self.project_urls_module.urlpatterns:
            if hasattr(mapping, 'name'):
                if mapping.name == 'home':
                    index_mapping_exists = True

        self.assertTrue(index_mapping_exists,
                        f"{FAILURE_HEADER}The home URL mapping could not be found. Check your PROJECT'S urls.py module.{FAILURE_FOOTER}")
        self.assertEquals(reverse('arty:home'), '/arty/',
                          f"{FAILURE_HEADER}The home URL lookup failed. Check arty's urls.py module. You're missing something in there.{FAILURE_FOOTER}")

    # def test_response(self):
    #
    #     """
    #     Does the response from the server contain the required string?
    #     """
    #     response = self.client.get(reverse('arty:index'))
    #
    #     self.assertEqual(response.status_code, 200,
    #                      f"{FAILURE_HEADER}Requesting the index page failed. Check your URLs and view.{FAILURE_FOOTER}")
    #     self.assertContains(response, "arty says hey there partner!",
    #                         msg_prefix=f"{FAILURE_HEADER}The index view does not return the expected response. Be careful you haven't missed any punctuation, and that your cAsEs are correct.{FAILURE_FOOTER}")
    #
    # def test_for_about_hyperlink(self):
    #     """
    #     Does the response contain the about hyperlink required in the exercise?
    #     Checks for both single and double quotes in the attribute. Both are acceptable.
    #     """
    #     response = self.client.get(reverse('arty:index'))
    #
    #     single_quotes_check = '<a href=\'/arty/about/\'>About</a>' in response.content.decode() or '<a href=\'/arty/about\'>About</a>' in response.content.decode()
    #     double_quotes_check = '<a href="/arty/about/">About</a>' in response.content.decode() or '<a href="/arty/about">About</a>' in response.content.decode()
    #
    #     self.assertTrue(single_quotes_check or double_quotes_check,
    #                     f"{FAILURE_HEADER}We couldn't find the hyperlink to the /arty/about/ URL in your index page. Check that it appears EXACTLY as in the book.{FAILURE_FOOTER}")
    #

class AboutPageTests(TestCase):
    """
    Tests to check the about view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the about() view exist in arty's views.py module?
        """
        name_exists = 'about' in self.views_module_listing
        is_callable = callable(self.views_module.about)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}We couldn't find the view for your about view! It should be called about().{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Check you have defined your about() view correctly. We can't execute it.{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the about view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:about'), '/arty/about/',
                          f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class loginPageTests(TestCase):
    """
    Tests to check the login view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the login() view exist in arty's views.py module?
        """
        name_exists = 'login' in self.views_module_listing
        is_callable = callable(self.views_module.login)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No login view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable login() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the login view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:login'), '/arty/login/',
                          f"{FAILURE_HEADER}Your about URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class homePageTests(TestCase):
    """
    Tests to check the login view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the home() view exist in arty's views.py module?
        """
        name_exists = 'home' in self.views_module_listing
        is_callable = callable(self.views_module.home)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No home view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable home() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the login view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:home'), '/arty/',
                          f"{FAILURE_HEADER}Home URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class signUpPageTests(TestCase):
    """
    Tests to check the login view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the sign_up() view exist in arty's views.py module?
        """
        name_exists = 'sign_up' in self.views_module_listing
        is_callable = callable(self.views_module.sign_up)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No sign_up view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable sign_up() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the sign_up view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:sign_up'), '/arty/sign_up/',
                          f"{FAILURE_HEADER}Home URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class contactUsPageTests(TestCase):
    """
    Tests to check the login view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the home() view exist in arty's views.py module?
        """
        name_exists = 'contact_us' in self.views_module_listing
        is_callable = callable(self.views_module.contact_us)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No contact us view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable contact_us() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:contact_us'), '/arty/contact_us/',
                          f"{FAILURE_HEADER}Home URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class myAccountPageTests(TestCase):
    """
    Tests to check the login view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'my_account' in self.views_module_listing
        is_callable = callable(self.views_module.my_account)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No my account us view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable my_account() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the login view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:my_account'), '/arty/my_account/',
                          f"{FAILURE_HEADER}My account URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class addPiecePageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'add_piece' in self.views_module_listing
        is_callable = callable(self.views_module.add_piece)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No add_piece view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable add_piece() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:add_piece'), '/arty/my_account/add_piece',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class addGalleryPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'add_gallery' in self.views_module_listing
        is_callable = callable(self.views_module.add_gallery)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No add_gallery view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable add_gallery() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:add_gallery'), '/arty/my_account/add_gallery',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class manageUsersPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'manage_users' in self.views_module_listing
        is_callable = callable(self.views_module.manage_users)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No manage_users view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable manage_users() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:manage_users'), '/arty/my_account/manage_users',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class editDetailsPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'edit_details' in self.views_module_listing
        is_callable = callable(self.views_module.edit_details)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No edit details view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable edit_details() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:edit_details'), '/arty/my_account/edit_details',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class postsPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'posts' in self.views_module_listing
        is_callable = callable(self.views_module.posts)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No posts view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable posts() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:posts'), '/arty/my_account/posts',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class categoryPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'category' in self.views_module_listing
        is_callable = callable(self.views_module.category)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No category view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable category() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:category'), '/arty/category/',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class showCategoryPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'show_category' in self.views_module_listing
        is_callable = callable(self.views_module.show_category)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No show_category view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable show_category() function{FAILURE_FOOTER}")

    # # can test all mappings like this?
    # def test_mapping_exists(self):
    #     """
    #     Checks whether the view has the correct URL mapping.
    #     """
    #     self.assertEquals(reverse('arty:show'), '/arty/contact_us/',
    #                       f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class addCategoryPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'add_category' in self.views_module_listing
        is_callable = callable(self.views_module.add_category)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No add_category view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable add_category() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:add_category'), '/arty/add_category/',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class galleryPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'galleries' in self.views_module_listing
        is_callable = callable(self.views_module.galleries)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No contact us view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable contact_us() function{FAILURE_FOOTER}")

    # can test all mappings like this?
    def test_mapping_exists(self):
        """
        Checks whether the view has the correct URL mapping.
        """
        self.assertEquals(reverse('arty:galleries'), '/arty/gallery/',
                          f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class showGalleryPageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'show_gallery' in self.views_module_listing
        is_callable = callable(self.views_module.show_gallery)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No contact us view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable show_gallery() function{FAILURE_FOOTER}")

    # # can test all mappings like this?
    # def test_mapping_exists(self):
    #     """
    #     Checks whether the view has the correct URL mapping.
    #     """
    #     self.assertEquals(reverse('arty:show_'), '/arty/contact_us',
    #                       f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class showPiecePageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'show_piece' in self.views_module_listing
        is_callable = callable(self.views_module.show_piece)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No show piece view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable show_piece() function{FAILURE_FOOTER}")

    # # can test all mappings like this?
    # def test_mapping_exists(self):
    #     """
    #     Checks whether the view has the correct URL mapping.
    #     """
    #     self.assertEquals(reverse('arty:show_'), '/arty/contact_us',
    #                       f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class showPiecePageTests(TestCase):
    """
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'show_piece' in self.views_module_listing
        is_callable = callable(self.views_module.show_piece)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No show piece view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable show_piece() function{FAILURE_FOOTER}")

    # # can test all mappings like this?
    # def test_mapping_exists(self):
    #     """
    #     Checks whether the view has the correct URL mapping.
    #     """
    #     self.assertEquals(reverse('arty:show_'), '/arty/contact_us',
    #                       f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")


class showReviewPageTests(TestCase):
    """
    wait
    Tests to check view.
    We check whether the view exists, the mapping is correct, and the response is correct.
    """

    def setUp(self):
        self.views_module = importlib.import_module('artyParty.views')
        self.views_module_listing = dir(self.views_module)

    def test_view_exists(self):
        """
        Does the view exist in arty's views.py module?
        """
        name_exists = 'show_review' in self.views_module_listing
        is_callable = callable(self.views_module.show_review)

        self.assertTrue(name_exists,
                        f"{FAILURE_HEADER}No contact us view.{FAILURE_FOOTER}")
        self.assertTrue(is_callable,
                        f"{FAILURE_HEADER}Unexecutable show_review() function{FAILURE_FOOTER}")

    # # can test all mappings like this?
    # def test_mapping_exists(self):
    #     """
    #     Checks whether the view has the correct URL mapping.
    #     """
    #     self.assertEquals(reverse('arty:show_'), '/arty/contact_us',
    #                       f"{FAILURE_HEADER} URL mapping is either missing or mistyped.{FAILURE_FOOTER}")

    #         index_path = os.path.join(self.artyParty_templates_dir, 'index.html')

    # def test_for_index_hyperlink(self):
    #     """
    #     Does the response contain the index hyperlink required in the exercise?
    #     Checks for both single and double quotes in the attribute. Both are acceptable.
    #     """
    #     response = self.client.get(reverse('arty:about'))
    #
    #     single_quotes_check = '<a href=\'/arty/\'>Index</a>' in response.content.decode()
    #     double_quotes_check = '<a href="/arty/">Index</a>' in response.content.decode()
    #
    #     self.assertTrue(single_quotes_check or double_quotes_check,
    #                     f"{FAILURE_HEADER}We could not find a hyperlink back to the index page in your about view. Check your about.html template, and try again.{FAILURE_FOOTER}")


class TemplatesStructureTests(TestCase):
    """
    Have you set templates, static files and media files up correctly, as per the book?
    """

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.templates_dir = os.path.join(self.project_base_dir, 'templates')
        self.artyParty_templates_dir = os.path.join(self.templates_dir, 'artyParty')

    def test_templates_directory_exists(self):
        """
        Does the templates/ directory exist?
        """
        directory_exists = os.path.isdir(self.templates_dir)
        self.assertTrue(directory_exists,
                        f"{FAILURE_HEADER}Your project's templates directory does not exist.{FAILURE_FOOTER}")

    def test_artyParty_templates_directory_exists(self):
        """
        Does the templates/artyParty/ directory exist?
        """
        directory_exists = os.path.isdir(self.artyParty_templates_dir)
        self.assertTrue(directory_exists,
                        f"{FAILURE_HEADER}The artyParty templates directory does not exist.{FAILURE_FOOTER}")

    def test_template_dir_setting(self):
        """
        Does the TEMPLATE_DIR setting exist, and does it point to the right directory?
        """
        variable_exists = 'TEMPLATE_DIR' in dir(settings)
        self.assertTrue(variable_exists,
                        f"{FAILURE_HEADER}Your settings.py module does not have the variable TEMPLATE_DIR defined!{FAILURE_FOOTER}")

        template_dir_value = os.path.normpath(settings.TEMPLATE_DIR)
        template_dir_computed = os.path.normpath(self.templates_dir)
        self.assertEqual(template_dir_value, template_dir_computed,
                         f"{FAILURE_HEADER}Your TEMPLATE_DIR setting does not point to the expected path. Check your configuration, and try again.{FAILURE_FOOTER}")

    def test_template_lookup_path(self):
        """
        Does the TEMPLATE_DIR value appear within the lookup paths for templates?
        """
        lookup_list = settings.TEMPLATES[0]['DIRS']
        found_path = False

        for entry in lookup_list:
            entry_normalised = os.path.normpath(entry)

            if entry_normalised == os.path.normpath(settings.TEMPLATE_DIR):
                found_path = True

        self.assertTrue(found_path,
                        f"{FAILURE_HEADER}Your project's templates directory is not listed in the TEMPLATES>DIRS lookup list. Check your settings.py module.{FAILURE_FOOTER}")

    def test_templates_exist(self):
        """
        Do the index.html and about.html templates exist in the correct place?
        """
        template_paths = ['about.html',
                          'add_comments.html',
                          'add_galleries.html',
                          'add_pieces.html',
                          'base.html',
                          'contact_us.html',
                          'gallery.html',
                          'get_gallery_list.html',
                          'get_piece_list.html',
                          'homepage.html',
                          'login.html',
                          'manage_users.html',
                          'myaccount.html',
                          'piece.html',
                          'pieces.html',
                          'post.html',
                          'sign_up.html']

        for path in template_paths:
            joined_path = os.path.join(self.artyParty_templates_dir, path)

            self.assertTrue(os.path.isfile(joined_path),
                            f"{FAILURE_HEADER} {path} template does not exist, or is in the wrong location.{FAILURE_FOOTER}")

# class TemplateTests(TestCase):
#     """
#     A series of tests to ensure that the index page/view has been updated to work with templates.
#     Image tests are in the Chapter4StaticMediaTests suite.
#     """
#
#     def setUp(self):
#         self.response = self.client.get(reverse('artyParty:index'))
#         template_paths = ['about.html',
#                           'add_comments.html',
#                           'add_galleries.html',
#                           'add_pieces.html',
#                           'base.html',
#                           'contact_us.html',
#                           'gallery.html',
#                           'get_gallery_list.html',
#                           'get_piece_list.html',
#                           'homepage.html',
#                           'login.html',
#                           'manage_users.html',
#                           'myaccount.html',
#                           'piece.html',
#                           'pieces.html',
#                           'post.html',
#                           'sign_up.html']
#
#
#     def test_index_uses_template(self):
#         """
#         Checks whether the index view uses a template -- and the correct one!
#         """
#         self.assertTemplateUsed(self.response, 'artyParty/index.html',
#                                 f"{FAILURE_HEADER}Your index() view does not use the expected index.html template.{FAILURE_FOOTER}")
#
#     def test_index_uses_context_dictionary(self):
#         """
#         Tests whether the index view uses the context dictionary correctly.
#         Crunchy, creamy cookie, anyone?
#         """
#         self.assertTrue('boldmessage' in self.response.context,
#                         f"{FAILURE_HEADER}In your index view, the context dictionary is not passing the boldmessage key. Check your context dictionary in the index() view, located in artyParty/views.py, and try again.{FAILURE_FOOTER}")
#
#         message = self.response.context['boldmessage']
#         expected = 'Crunchy, creamy, cookie, candy, cupcake!'
#         self.assertEqual(message, expected,
#                          f"{FAILURE_HEADER}The boldmessage being sent to the index.html template does not match what is expected. Check your index() view. Make sure you match up cases, and don't miss any punctuation! Even one missing character will cause the test to fail.{FAILURE_FOOTER}")
#
#     def test_index_starts_with_doctype(self):
#         """
#         Is the <!DOCTYPE html> declaration on the first line of the index.html template?
#         """
#         self.assertTrue(self.response.content.decode().startswith('<!DOCTYPE html>'),
#                         f"{FAILURE_HEADER}Your index.html template does not start with <!DOCTYPE html> -- this is requirement of the HTML specification.{FAILURE_FOOTER}")
#
#     def test_about_link_present(self):
#         """
#         Is the about hyperlink present and correct on the index.html template?
#         """
#         expected = "<a href=\"/artyParty/about/\">About</a><br />"
#         self.assertTrue(expected in self.response.content.decode(),
#                         f"{FAILURE_HEADER}Your index.html template doesn't contain the /artyParty/about/ link -- or it is not correct. Make sure you have the linebreak in, too!{FAILURE_FOOTER}")
#

class ArtyStaticMediaTests(TestCase):
    """
    A series of tests to check whether static files and media files have been setup and used correctly.
    Also tests for the two required files -- artyParty.jpg and cat.jpg.
    """

    def setUp(self):
        self.project_base_dir = os.getcwd()
        self.static_dir = os.path.join(self.project_base_dir, 'static')
        self.media_dir = os.path.join(self.project_base_dir, 'media')

    def test_does_static_directory_exist(self):
        """
        Tests whether the static directory exists in the correct location -- and the images subdirectory.
        Also checks for the presence of artyParty.jpg in the images subdirectory.
        """
        does_static_dir_exist = os.path.isdir(self.static_dir)
        does_images_static_dir_exist = os.path.isdir(os.path.join(self.static_dir, 'images'))
        #does_artyParty_jpg_exist = os.path.isfile(os.path.join(self.static_dir, 'images', 'artyParty.jpg'))

        self.assertTrue(does_static_dir_exist,
                        f"{FAILURE_HEADER}The static directory was not found in the expected location. Check the instructions in the book, and try again.{FAILURE_FOOTER}")
        self.assertTrue(does_images_static_dir_exist,
                        f"{FAILURE_HEADER}The images subdirectory was not found in your static directory.{FAILURE_FOOTER}")
        # self.assertTrue(does_artyParty_jpg_exist,
        #                 f"{FAILURE_HEADER}We couldn't locate the artyParty.jpg image in the /static/images/ directory. If you think you've included the file, make sure to check the file extension. Sometimes, a JPG can have the extension .jpeg. Be careful! It must be .jpg for this test.{FAILURE_FOOTER}")

    def test_does_media_directory_exist(self):
        """
        Tests whether the media directory exists in the correct location.
        Also checks for the presence of cat.jpg.
        """
        does_media_dir_exist = os.path.isdir(self.media_dir)
        does_cat_jpg_exist = os.path.isfile(os.path.join(self.media_dir, 'cat.jpg'))

        self.assertTrue(does_media_dir_exist,
                        f"{FAILURE_HEADER}We couldn't find the /media/ directory in the expected location. Make sure it is in your project directory (at the same level as the manage.py module).{FAILURE_FOOTER}")

    def test_static_and_media_configuration(self):
        """
        Performs a number of tests on your Django project's settings in relation to static files and user upload-able files..
        """
        static_dir_exists = 'STATIC_DIR' in dir(settings)
        self.assertTrue(static_dir_exists,
                        f"{FAILURE_HEADER}Your settings.py module does not have the variable STATIC_DIR defined.{FAILURE_FOOTER}")

        expected_path = os.path.normpath(self.static_dir)
        static_path = os.path.normpath(settings.STATIC_DIR)
        self.assertEqual(expected_path, static_path,
                         f"{FAILURE_HEADER}The value of STATIC_DIR does not equal the expected path. It should point to your project root, with 'static' appended to the end of that.{FAILURE_FOOTER}")

        staticfiles_dirs_exists = 'STATICFILES_DIRS' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists,
                        f"{FAILURE_HEADER}The required setting STATICFILES_DIRS is not present in your project's settings.py module. Check your settings carefully. So many students have mistyped this one.{FAILURE_FOOTER}")
        self.assertEqual([static_path], settings.STATICFILES_DIRS,
                         f"{FAILURE_HEADER}Your STATICFILES_DIRS setting does not match what is expected. Check your implementation against the instructions provided.{FAILURE_FOOTER}")

        staticfiles_dirs_exists = 'STATIC_URL' in dir(settings)
        self.assertTrue(staticfiles_dirs_exists,
                        f"{FAILURE_HEADER}The STATIC_URL variable has not been defined in settings.py.{FAILURE_FOOTER}")
        self.assertEqual('/static/', settings.STATIC_URL,
                         f"{FAILURE_HEADER}STATIC_URL does not meet the expected value of /static/. Make sure you have a slash at the end!{FAILURE_FOOTER}")

        media_dir_exists = 'MEDIA_DIR' in dir(settings)
        self.assertTrue(media_dir_exists,
                        f"{FAILURE_HEADER}The MEDIA_DIR variable in settings.py has not been defined.{FAILURE_FOOTER}")

        expected_path = os.path.normpath(self.media_dir)
        media_path = os.path.normpath(settings.MEDIA_DIR)
        self.assertEqual(expected_path, media_path,
                         f"{FAILURE_HEADER}The MEDIA_DIR setting does not point to the correct path. Remember, it should have an absolute reference to wad_2_team_project/media/.{FAILURE_FOOTER}")

        media_root_exists = 'MEDIA_ROOT' in dir(settings)
        self.assertTrue(media_root_exists,
                        f"{FAILURE_HEADER}The MEDIA_ROOT setting has not been defined.{FAILURE_FOOTER}")

        media_root_path = os.path.normpath(settings.MEDIA_ROOT)
        self.assertEqual(media_path, media_root_path,
                         f"{FAILURE_HEADER}The value of MEDIA_ROOT does not equal the value of MEDIA_DIR.{FAILURE_FOOTER}")

        media_url_exists = 'MEDIA_URL' in dir(settings)
        self.assertTrue(media_url_exists,
                        f"{FAILURE_HEADER}The setting MEDIA_URL has not been defined in settings.py.{FAILURE_FOOTER}")

        media_url_value = settings.MEDIA_URL
        self.assertEqual('/media/', media_url_value,
                         f"{FAILURE_HEADER}Your value of the MEDIA_URL setting does not equal /media/. Check your settings!{FAILURE_FOOTER}")

    def test_context_processor_addition(self):
        """
        Checks to see whether the media context_processor has been added to your project's settings module.
        """
        context_processors_list = settings.TEMPLATES[0]['OPTIONS']['context_processors']
        self.assertTrue('django.template.context_processors.media' in context_processors_list,
                        f"{FAILURE_HEADER}The 'django.template.context_processors.media' context processor was not included. Check your settings.py module.{FAILURE_FOOTER}")


# class Chapter4ExerciseTests(TestCase):
#     """
#     A series of tests to ensure that the exercise listing at the end of Chapter 4 has been completed.
#     """
#
#     def setUp(self):
#         self.project_base_dir = os.getcwd()
#         self.template_dir = os.path.join(self.project_base_dir, 'templates', 'artyParty')
#         self.about_response = self.client.get(reverse('artyParty:about'))
#
#     def test_about_template_exists(self):
#         """
#         Tests the about template -- if it exists, and whether or not the about() view makes use of it.
#         """
#         template_exists = os.path.isfile(os.path.join(self.template_dir, 'about.html'))
#         self.assertTrue(template_exists,
#                         f"{FAILURE_HEADER}The about.html template was not found in the expected location.{FAILURE_FOOTER}")
#
#     def test_about_uses_template(self):
#         """
#         Checks whether the index view uses a template -- and the correct one!
#         """
#         self.assertTemplateUsed(self.about_response, 'artyParty/about.html',
#                                 f"{FAILURE_HEADER}The about() view does not use the about.html template.{FAILURE_FOOTER}")
#
#     def test_about_starts_with_doctype(self):
#         """
#         Is the <!DOCTYPE html> declaration on the first line of the about.html template?
#         """
#         self.assertTrue(self.about_response.content.decode().startswith('<!DOCTYPE html>'),
#                         f"{FAILURE_HEADER}Your about.html template does not start with <!DOCTYPE html> -- this is requirement of the HTML specification.{FAILURE_FOOTER}")
#
#     def test_about_contains_required_text(self):
#         """
#         Checks to see whether the required text is on the rendered about page.
#         """
#         required = [
#             "here is the about page.",
#             "This tutorial has been put together by "
#         ]
#
#         for required_str in required:
#             self.assertTrue(required_str in self.about_response.content.decode(),
#                             f"{FAILURE_HEADER}The expected string '{required_str}' was not found in the rendered /artyParty/about/ response.{FAILURE_FOOTER}")
#
#     def test_about_contains_artyParty(self):
#         """
#         Checks whether the rendered about view has the picture of artyParty.
#         """
#         required_str = f"<img src=\"{settings.STATIC_URL}images/artyParty.jpg\" alt=\"Picture of artyParty\" />"
#         self.assertTrue(required_str in self.about_response.content.decode(),
#                         f"{FAILURE_HEADER}The HTML markup to include the image of artyParty in the about template was not found. It needs to match exactly what we are looking for. Check the book.{FAILURE_FOOTER}")
#
#     def test_about_contains_cat(self):
#         """
#         Checks whether the rendered about view has the picture of a cat.
#         We need to be a little bit lenient here as the example above includes a period, and in the exercise instructions, the required alt text is ended with a period. Either with or without is acceptable.
#         """
#         required_pattern = f"<img src=\"{settings.MEDIA_URL}cat.jpg\" alt=\"Picture of a Cat.?\" />"
#         self.assertTrue(re.search(required_pattern, self.about_response.content.decode()),
#                         f"{FAILURE_HEADER}The HTML markup to include the image of a cat in the about template was not found. It needs to match exactly what we are looking for. Check the book.{FAILURE_FOOTER}")
