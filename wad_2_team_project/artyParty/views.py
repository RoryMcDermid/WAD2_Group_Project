from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("This is the home")


def user_login(request):
    return HttpResponse("Login")


def user_sign_up(request):
    return HttpResponse("Sign Up Here")


def about(request):
    return HttpResponse("About")


def contact_us(request):
    return HttpResponse("Contact Us")


def my_account(request):
    return HttpResponse("My Account")


def add_piece(request):
    return HttpResponse("Add Piece")


def add_gallery(request):
    return HttpResponse("Add Gallery")


def manage_users(request):
    return HttpResponse("Manage Users")


def edit_details(request):
    return HttpResponse("Edit details")


def posts(request):
    return HttpResponse("View Posts")


def category(request):
    return HttpResponse("Category (is)")


def add_category(request):
    return HttpResponse("Add Category")

def show_category(request):
    return HttpResponse("Add Piece")


def gallery(request):
    return HttpResponse("Galleries page I think?")


def show_gallery(request):
    return HttpResponse("Here's a gallery")


def show_piece(request):
    return HttpResponse("Showing piece")


def show_review(request):
    return HttpResponse("Showing Review")

