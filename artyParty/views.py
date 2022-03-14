from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # top 4 peices ordered by popularity
    # change template to display them line 11
    return render(request, 'artyParty/homepage.html', context={})


def user_login(request):
    # can we copy from rango?

    return HttpResponse("Login")


def sign_up(request):
    # copy from rango
    return HttpResponse("Sign Up Here")


def about(request):
    # no real need for context come back to
    #

    return HttpResponse("About")


def contact_us(request):
    # what happens to submitted form? -> maybe put into db?
    # redirect to homepage
    return HttpResponse("Contact Us")


def my_account(request):
    # @loginrequired decorator
    #
    return HttpResponse("My Account")


def add_piece(request):
    # take from rango
    return HttpResponse("Add Piece")


def add_gallery(request):
    # from rango
    return HttpResponse("Add Gallery")


def manage_users(request):
    # for power users
    return HttpResponse("Manage Users")


def edit_details(request):
    # ???????
    return HttpResponse("Edit details")


def posts(request):
    # what is this posts page about? Is this where we post info?

    return HttpResponse("View Posts")
    # res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Christ_of_Saint_John_of_the_Cross")
    # data = res.json()
    # context_dict = {'descript': data['extract']}
    # return render(request, "View Posts", context_dict)

# CATEGORIES MAYBE ADD LATER, BUT LIKE FUCK THAT RN

# def category(request):
#     # show all peices in given category
#     # qurey db for peices where category == passed value
#
#     return HttpResponse("Category (is)")
#
#
# def add_category(request):
#
#     return HttpResponse("Add Category")
#
# def show_category(request):
#     return HttpResponse("Add Piece")


def pieces(request):
    # querey db for all pieces where gallery == passed val
    #
    return HttpResponse("Galleries page I think?")


def show_gallery(request):
    ## see rango show_category
    return HttpResponse("Here's a gallery")


def show_piece(request):
    ## see rango show_category
    return HttpResponse("Showing piece")


def show_review(request):
    ## see rango show_category
    return HttpResponse("Showing Review")

