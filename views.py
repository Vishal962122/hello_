# bulk_upload/views.py

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the Bulk Upload App!</h1>")
