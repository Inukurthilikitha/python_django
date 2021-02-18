from django import template
register = template.Library()

#https://django.readthedocs.io/en/1.2.X/howto/custom-template-tags.html

@register.filter(name='cutout')
@register.filter(name='cutout_another')

def cutout(value, arg):
    return value.replace(arg, '')

def cutout_another(value, arg):
    return value.replace(arg, '')

#register.filter('cutout',cutout) #other way to register filter