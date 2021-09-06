from django import template

register = template.Library()

@register.filter(name='addClass')
def addClass(value, arg):
    return value.as_widget(attrs={'class':arg})

@register.filter(name='addZero')
def addClass(value):
    return str(value).zfill(3)

@register.filter(name='addDisable')
def addClass(value, arg):
    return value.as_widget(attrs={' ':arg})