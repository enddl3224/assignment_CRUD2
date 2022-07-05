from django.shortcuts import render

import json

from django.http import JsonResponse
from django.views import View

from owners.models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data      = json.loads(request.body)
        Owner.objects.create(name=data['owner'],email=data['email'],age=data['age'])
        
        return JsonResponse({'messasge':'created'}, status=201)

# Create your views here.


class DogsView(View):
    def post(self, request):
        data      = json.loads(request.body)
        
        Dog.objects.create(
            name = data['dog'],
            age=data['age'],
            owner_id = data['ownerid']
        )
        return JsonResponse({'messasge':'created'}, status=201)