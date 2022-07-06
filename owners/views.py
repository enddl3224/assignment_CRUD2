from unicodedata import name
from unittest import result
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

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs=Dog.objects.filter(owner=owner)
            results2=[]

            for dog in dogs:
                dog_imfomation={
                        'name' : dog.name,
                        'age':dog.age
                    }
                results2.append(dog_imfomation)

            owner_information={
                    "owner": owner.name,
                    "email":owner.email,
                    "age": owner.age,
                    "dogs":results2
                }
            results.append(owner_information)
            
       
        return JsonResponse({'resutls':results}, status=200)

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

    def get(self, request):
        dogs = Dog.objects.all() #데이터베이스에서 강아지 정보를 전부 갖고 온다.
        results  = [] #result에 빈 배열 할당

        for dog in dogs:    #객체 하나하나 뽑기
           results.append(
               {
                   "dog" : dog.name,
                   "age" : dog.age,
                   "owner" : dog.owner_id
               }
           )
       
        return JsonResponse({'resutls':results}, status=200)


    