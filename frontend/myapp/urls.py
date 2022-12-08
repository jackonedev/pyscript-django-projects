from django.urls import path

from .views import PyScriptHandlerView

app_name = 'myapp'

urlpatterns = [
    path('', PyScriptHandlerView.as_view(), name='pyscript-handler'),
]