from django.urls import path

from .views import PyScriptHandlerView

urlpatterns = [
    path('', PyScriptHandlerView.as_view(), name='pyscript-handler'),
]