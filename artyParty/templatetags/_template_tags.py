# from django import template
# from artyParty.models import Category
#
# register = template.Library()
#
# @register.inclusion_tag('rango/categories.html')
# def get_category_list():
#     return {'categories': Category.objects.all()}

from django import template
from artyParty.models import Category

register = template.Library()

@register.inclusion_tag('artyParty/get_gallery_list')
def get_gallery_list():
     return {'galleries': Gallery.objects.all()，
        'current_category': current_category}
            

@register.inclusion_tag('artyParty/get_piece_list')
def get_piece_list():
    return {'pieces': Piece.objects.all()}