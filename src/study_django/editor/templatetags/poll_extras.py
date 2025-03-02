from django import template

register = template.Library()


@register.filter
def get_attr(obj, attr_name):
    """
    Gets an attribute from an object, using getattr.

    If it does not exist, returns empty string
    """
    try:
        return getattr(obj, attr_name)
    except AttributeError:
        return ""


@register.filter
def multiply(obj, arg):
    return obj * arg
