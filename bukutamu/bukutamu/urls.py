
from django.contrib import admin
from django.urls import path

from django.http import HttpResponse

def buku(req):
    return HttpResponse('Unsulbar Informatika')

urlpatterns = [
    path('buku',buku),
    path('admin/', admin.site.urls),
]
