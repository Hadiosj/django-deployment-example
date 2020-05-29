from django import template

register=template.Library()
def cut(value,arg):
    #This cuts out all value of 'arg' from string
    return value.replace(arg,'000')

register.filter('cut',cut)
