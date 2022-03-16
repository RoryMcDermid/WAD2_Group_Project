from django.shortcuts import render
from django.http import HttpResponse

#maybe rename this or homepage to have the same name?
def home(request):
    # top 4 peices ordered by popularity
    # change template to display them line 11
    return render(request, 'artyParty/homepage.html', context={})


def login(request):
    # can we copy from rango?
    context_dict = {}

    return render(request, 'artyParty/login.html', context=context_dict)


def sign_up(request):
    context_dict = {}
    # copy from rango
    return render(request, 'artyParty/sign_up.html', context=context_dict)


def about(request):
    context_dict = {}
    # no real need for context come back to
    #

    return render(request, 'artyParty/about.html', context=context_dict)


def contact_us(request):
    # what happens to submitted form? -> maybe put into db?
    # redirect to homepage
    context_dict = {}

    return render(request, 'artyParty/contact_us.html', context=context_dict)


def my_account(request):
    # @loginrequired decorator
    #
    context_dict = {}

    return render(request, 'artyParty/myaccount.html', context=context_dict)


def add_piece(request):
    # take from rango
    context_dict = {}

    return render(request, 'artyParty/add_pieces.html', context=context_dict)


def add_gallery(request):
    # from rango
    context_dict = {}

    return render(request, 'artyParty/add_galleries.html', context=context_dict)



def manage_users(request):
    # for power users
    context_dict = {}

    return render(request, 'artyParty/manage_users.html', context=context_dict)



def edit_details(request):
    # ???????

    #needs template
    return HttpResponse("Edit details")


def posts(request):
    # what is this posts page about? Is this where we post info?

    context_dict = {}

    return render(request, 'artyParty/post.html', context=context_dict)

    # res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Christ_of_Saint_John_of_the_Cross")
    # data = res.json()
    # context_dict = {'descript': data['extract']}
    # return render(request, "View Posts", context_dict)

# CATEGORIES MAYBE ADD LATER, BUT LIKE FUCK THAT RN - james

def category(request):
    # show all peices in given category
    # qurey db for peices where category == passed value


    #needs template
    return HttpResponse("Category (is)")


def add_category(request):

    #needs template
    return HttpResponse("Add Category")

def show_category(request):

    #needs template
    return HttpResponse("Add Piece")


def galleries(request):
    # querey db for all pieces where gallery == passed val
    #
    context_dict = {}

    return render(request, 'artyParty/galleries.html', context=context_dict)



def show_gallery(request):
    ## see rango show_category
    context_dict = {}

    return render(request, 'artyParty/pieces.html', context=context_dict)



def show_piece(request):
    ## see rango show_category
    context_dict = {}

    # return render(request, 'artyParty/post.html', context=context_dict)

    res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Christ_of_Saint_John_of_the_Cross")
    data = res.json()
    context_dict = {'descript': data['extract']}
    # return render(request, "View Posts", context_dict)

    return render(request, 'artyParty/post.html', context=context_dict)



def show_review(request):
    ## see rango show_category

    #which template is this?
    return HttpResponse("Showing Review")

