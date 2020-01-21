from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.core import serializers

from .models import mydb
import json

class db(mydb):
    
    @classmethod
    def get(pk):
        obj_json = serializers.serialize('json', mydb.objects.filter(pk=pk))
        json_data = json.loads(obj_json)
        return str(json_data[0]['fields'])

    @classmethod
    def update(pk, json_data):
        mydb.objects.filter(pk=pk).update(
            field=json_data['field'],
            type=json_data['type'],
            default=json_data['default'],
            value=json_data['value']
        )