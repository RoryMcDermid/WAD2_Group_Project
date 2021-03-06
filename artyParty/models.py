from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    USER_TYPE_MAX_LENGTH = 5

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    userID = models.IntegerField(unique=True, blank=False)

    def __str__(self):
        return self.user.username


class Gallery(models.Model):
    GALLERY_NAME_MAX_LENGTH = 50

    gallery_name = models.CharField(max_length=GALLERY_NAME_MAX_LENGTH, blank=False)
    gallery_id = models.IntegerField(unique=True, blank=False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery_img = models.ImageField(blank=False, upload_to='artyParty_images')
    gallery_description = models.TextField(blank=True)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.gallery_name)
        super(Gallery, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Galleries'

    def __str__(self):
        return str(self.gallery_id)


class Piece(models.Model):
    PIECE_NAME_MAX_LENGTH = 50
    PIECE_CATEGORY_MAX_LENGTH = 20
    MAX_AUTHOR_LENGTH = 20

    gallery_id = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    piece_img = models.ImageField(blank=False, upload_to='artyParty_images')
    piece_id = models.IntegerField(unique=True, blank=False)
    piece_name = models.CharField(max_length=PIECE_NAME_MAX_LENGTH, blank=False)
    author = models.CharField(max_length=MAX_AUTHOR_LENGTH, blank=False)
    period = models.CharField(max_length=PIECE_CATEGORY_MAX_LENGTH, blank=False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.piece_name)
        super(Piece, self).save(*args, **kwargs)

    def __str__(self):
        return (str(self.piece_name))


class Review(models.Model):
    review_id = models.IntegerField(unique=True, )
    piece_id = models.ForeignKey(Piece, on_delete=models.CASCADE, blank=False)
    rating = models.IntegerField(blank=False)
    userID = models.ForeignKey(User, on_delete=models.CASCADE, )
    review = models.TextField()

    def __str__(self):
        return self.review[:10]
