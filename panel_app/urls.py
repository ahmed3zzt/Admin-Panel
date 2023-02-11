from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse('Hello App')

urlpatterns = [
    path('',test,name='home')
]
