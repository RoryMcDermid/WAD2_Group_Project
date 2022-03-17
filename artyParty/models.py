from django.db import models
from django.template.defaultfilters import slugify


class User(models.Model):
    USER_NAME_MAX_LENGTH = 50
    USER_TYPE_MAX_LENGTH = 5
    
    user_id = models.IntegerField(unique=True, blank=False)
    user_name = models.CharField(max_length=USER_NAME_MAX_LENGTH, blank=False)
    user_type = models.CharField(max_length=USER_TYPE_MAX_LENGTH, blank=False)

    def __str__(self):
        return self.user_id


class Gallery(models.Model):
    GALLERY_NAME_MAX_LENGTH = 50

    gallery_id = models.IntegerField(unique=True, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery_name = models.CharField(max_length=GALLERY_NAME_MAX_LENGTH, blank=False)
    gallery_description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.gallery_name)
        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return self.gallery_id


class Piece(models.Model):
    PIECE_NAME_MAX_LENGTH = 50
    PIECE_CATEGORY_MAX_LENGTH = 20

    piece_img = models.ImageField(blank=False, upload_to='artyParty_images')
    piece_id = models.IntegerField(unique=True, blank=False)
    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    piece_name = models.CharField(max_length=PIECE_NAME_MAX_LENGTH, blank=False)
    piece_category = models.CharField(max_length=PIECE_CATEGORY_MAX_LENGTH, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.piece_id


class Review(models.Model):

    review_id = models.IntegerField(unique=True, blank=False)
    piece_id = models.ForeignKey(Piece, on_delete=models.CASCADE, blank=False)
    rating = models.IntegerField(blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    review = models.TextField

    def __str__(self):
        return self.review_id
