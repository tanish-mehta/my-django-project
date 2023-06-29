from django.conf import settings
import os

from django.http import HttpResponse

def index(request):
    with open(os.path.join(settings.BASE_DIR, 'frontend', 'build', 'index.html')) as f:
        return HttpResponse(f.read())
