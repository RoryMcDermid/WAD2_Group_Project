from django.contrib import admin
from artyParty.models import User, Gallery, Piece, Review


class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'user_type')


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('gallery_name',)}
    list_display = ('gallery_name', 'gallery_id', 'gallery_description', 'user_id')


class PieceAdmin(admin.ModelAdmin):
    list_display = ('piece_img', 'piece_id', 'gallery_id', 'piece_name', 'author', 'period', 'user_id')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'piece_id', 'rating', 'user_id', 'review')


admin.site.register(User, UserAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Review, ReviewAdmin)
