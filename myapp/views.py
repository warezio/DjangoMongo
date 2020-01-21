from django.shortcuts import render, get_object_or_404, redirect
from django.core import serializers

from .models import mydb
from .forms import mydbForm

# Import db_helper as db
from .db_helper import db
import json

def data_list(request):
    datas = mydb.objects.all()
    return render(request, 'myapp/data_list.html', {'datas': datas})

def data_add(request):
    if request.method == "POST":
        form = mydbForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect('data_change', pk=data.pk)
    else:
        form = mydbForm()
    return render(request, 'myapp/data_edit.html', {'form': form})

def data_change(request, pk):
    data = get_object_or_404(mydb, pk=pk)
    # Call db.get by key
    data_json = db.get(pk=pk)
    if request.method == "POST":
        form = mydbForm(request.POST, instance=data)
        if form.is_valid():
            data = form.save(commit=False)
            # data.save()
            obj_json = serializers.serialize('json', data.fields)
            json_data = json.dumps(obj_json)
            # Call db.update with key and json
            db.update(pk=pk, json_data=json_data)
            return redirect('data_change', pk=data.pk)
    else:
        form = mydbForm(instance=data)
    return render(request, 'myapp/data_edit.html', {'data': data, 'form': form, 'data_json': data_json})
