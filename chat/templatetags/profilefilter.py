from django import template
from users.models import  Profile
register = template.Library()

@register.filter('profilefilter')
def profile(value,id):
    try:
        instance  =  Profile.objects.get(user=id)
        return instance.image
    except:
        return None
