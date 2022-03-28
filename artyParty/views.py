from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from artyParty.forms import UserForm, UserProfileForm, EditUserForm, AddReviewForm
import requests
from artyParty.models import Piece, Gallery, Review
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.http import JsonResponse


# maybe rename this or homepage to have the same name?
def home(request):
    # top 4 pieces ordered by popularity
    # change template to display them line 11

    # need to change carosel to images from galleries
    # need to figure out how to sort by rating
    piece_list = Piece.objects.order_by('-piece_id')[:4]
    galleries = Gallery.objects.all()

    context_dict = {}

    context_dict['pieces'] = piece_list
    context_dict['gallery'] = galleries

    return render(request, 'artyParty/homepage.html', context=context_dict)


def user_login(request):
    # can we copy from rango?

    ############################################################################
    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        # We use request.POST.get('<variable>') as opposed
        # to request.POST['<variable>'], because the
        # request.POST.get('<variable>') returns None if the
        # value does not exist, while request.POST['<variable>']
        # will raise a KeyError exception.
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)
        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return redirect(reverse('arty:home'))
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your artyParty account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'artyParty/login.html')
    ############################################################################


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('arty:home'))


def sign_up(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves,
            # we set commit=False. This delays saving the model
            # until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful.
            registered = True
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # Not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request, 'artyParty/sign_up.html',
                    context={'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
    ############################################################################


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


@login_required
def my_account(request):
    # @loginrequired decorator

    form = EditUserForm(instance = request.user)


    context_dict = {

    }

    # context_dict[''] =

    return render(request, 'artyParty/myaccount.html', context=context_dict)


@login_required
def add_piece(request):
    # take from rango
    context_dict = {}

    return render(request, 'artyParty/add_pieces.html', context=context_dict)


@login_required
def add_gallery(request):
    # from rango
    context_dict = {}

    return render(request, 'artyParty/add_galleries.html', context=context_dict)


@login_required
def manage_users(request):
    # for power users
    context_dict = {}

    return render(request, 'artyParty/manage_users.html', context=context_dict)


@login_required
def edit_details(request):

    message = ""
    if request.method == 'POST':

        user_form = EditUserForm(request.POST, instance = request.user)

        if user_form.is_valid():

            user_form.save()
            message = "Details updated"

        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(user_form.errors)

    form = EditUserForm(instance = request.user)

    context_dict = {
        "form":form,
        "message":message,
    }


    return render(request, 'artyParty/edit_details.html', context=context_dict)


def posts(request):
    # what is this posts page about? Is this where we post info?

    context_dict = {}

    return render(request, 'artyParty/post.html', context=context_dict)

    # res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/Christ_of_Saint_John_of_the_Cross")
    # data = res.json()
    # context_dict = {'descript': data['extract']}
    # return render(request, "View Posts", context_dict)


def galleries(request):
    ## see rango show_category

    gallery_list = Gallery.objects.order_by("gallery_id")  # this 3 needs to be the length of gallery

    context_dict = {'galleries': gallery_list}
    return render(request, 'artyParty/get_gallery_list.html', context=context_dict)


def show_gallery(request, gallery_name_slug):
    # see rango show_category
    # querey db for all pieces where gallery == passed val
    context_dict = {}
    try:
        gallery = Gallery.objects.get(slug=gallery_name_slug)
        pieces = Piece.objects.filter(gallery_id=gallery)
        context_dict['pieces'] = pieces
        context_dict['gallery'] = gallery
        ctx = {}
        for p in pieces:
            link = "https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(p.slug.replace("-", "_"))
            res = requests.get(link)
            data = res.json()
            extract = data['extract']
            ctx[p.slug] = extract
        context_dict['ctx'] = ctx

    except Gallery.DoesNotExist:
        context_dict['pieces'] = None
        context_dict['gallery'] = None

    return render(request, 'artyParty/gallery.html', context=context_dict)


def piece(request, gallery_name_slug, piece_name_slug):
    ## see rango show_category
    context_dict = {}
    try:
        p = Piece.objects.get(slug=piece_name_slug)
        gallery = Gallery.objects.get(slug=gallery_name_slug)
        context_dict['piece'] = p
        context_dict['gallery'] = gallery
        res = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/{}".format(p.slug.replace("-", "_")))
        data = res.json()
        extract = data['extract']
        context_dict['extract'] = extract
        reviews = Review.objects.filter(piece_id_id=p)
        context_dict['reviews'] = reviews
        r = {}
        for review in reviews:
            r[review.review_id] = range(review.rating)
        context_dict['range'] = r

    except Piece.DoesNotExist:
        context_dict['piece'] = None
        context_dict['gallery'] = None
    return render(request, 'artyParty/piece.html', context=context_dict)

def show_review(request):
    ## see rango show_category

    # which template is this?
    # return render(request, 'artyParty/show_review.html', context=context_dict)
    return HttpResponse("Showing Review")


def add_review(request, piece_name_slug, gallery_name_slug):
    ## see rango show_category
    message = ""
    piece = Piece.objects.get(slug=piece_name_slug)
    if request.method == 'POST':


        review_form = AddReviewForm(request.POST)

        if review_form.is_valid():



            review = review_form.save(commit = False)

            review.piece_id = piece

            user = request.user

            review.userID_id = user.id

            max = 0
            for reviews in Review.objects.all():
                if reviews.review_id > max:
                    max = reviews.review_id

            review.review_id = max + 1

            review.save()

            message = "Review Added"


            return redirect(reverse('arty:piece', kwargs={'gallery_name_slug':gallery_name_slug, 'piece_name_slug':piece_name_slug}))
        else:
            # Invalid form or forms - mistakes or something else?
            # Print problems to the terminal.
            print(review_form.errors)

    form = AddReviewForm()

    context_dict = {
        "form":form,
        "message":message,
    }

    gallery = Gallery.objects.get(slug=gallery_name_slug)
    context_dict['piece'] = piece
    context_dict['gallery'] = gallery
    # which template is this?
    return render(request, 'artyParty/add_review.html', context=context_dict)
    # return HttpResponse("Showing Review")
