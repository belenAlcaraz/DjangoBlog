from django import template
import markdown as md

register = template.Library()

@register.filter(name='markdown')
def markdown(text):
    return md.markdown(text, extensions=['fenced_code','codehillite'])