from django.shortcuts import render
from django.views.generic import View


class PyScriptHandlerView(View):
    def get(self, request):
        return render(request, 'myapp/index.html')

    # def post(self, request):
    #     return render(request, 'myapp/index.html')