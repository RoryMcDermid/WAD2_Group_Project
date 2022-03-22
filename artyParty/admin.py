from django.contrib import admin
from artyParty.models import UserProfile
from artyParty.models import Gallery, Piece, Review


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('gallery_name',)}
    list_display = ('gallery_name', 'gallery_id', 'gallery_description', 'userID')


class PieceAdmin(admin.ModelAdmin):
    list_display = ('piece_img', 'piece_id', 'gallery_id', 'piece_name', 'author', 'period', 'userID')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'piece_id', 'rating', 'userID', 'review')


admin.site.register(UserProfile)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Review, ReviewAdmin)
