"""wad_2_team_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from artyParty import views


urlpatterns = [
    path('', views.home, name='home'),
    path('arty/', include('artyParty.urls')),
    # check how folders are working on thursday"""
    path('admin/', admin.site.urls),
]

"""
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('sign_up/', views.user_sign_up, name='sign_up'),
    path('about/', views.about, name = 'about'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('my_account/', views.my_account, name = 'my_account'),
    path('my_account/add_piece', views.add_piece, name = 'add_piece'),
    path('my_account/add_gallery', views.add_gallery, name = 'add_gallery'),
    path('my_account/manage_users', views.manage_users, name = 'manage_users'),
    path('my_account/edit_details', views.edit_details, name = 'edit_details'),
    path('my_account/posts', views.posts, name = 'posts'),
    path('category/', views.category, name='category'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('gallery/', views.gallery, name='gallery'),
    path('gallery/<slug:gallery_name_slug>/', views.show_gallery, name='show_gallery'),
    path('gallery/<slug:gallery_name_slug>/<slug:piece_name_slug>/', views.show_piece, name='show_piece'),
    path('gallery/<slug:gallery_name_slug>/<slug:piece_name_slug>/<slug:review_name_slug>/', views.show_review, name='show_review'),
    
    # think this is in twice
    #path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),


    saved for ArtyParty views.py


"""