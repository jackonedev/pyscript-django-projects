from random import randint
import json

from django.shortcuts import render
from django.views.generic import View

from django.http import JsonResponse

class PyScriptHandlerView(View):
    def get(self, request):
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':

            number = randint(1, 10)
            return JsonResponse({'number': number})

        return render(request, 'myapp/index.html')


    def post(self, request):
        number = json.loads(request.body)['number']
        return JsonResponse({'data': f'You sent {float(number)}'})