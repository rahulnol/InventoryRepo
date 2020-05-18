import json

from django import template

register = template.Library()

@register.simple_tag
def convert_ordereddict_to_json(data):
    return json.dumps(data)


def convertDictToJson(value):
    jsonData = json.dumps(value)
    return jsonData

register.filter('myDitToJson',convertDictToJson)


register.filter('dictToJson',convert_ordereddict_to_json)

