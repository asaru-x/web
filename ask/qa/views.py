from django.http import HttpResponse

# Create your views here.

def handler(request):
    return HttpResponse('[OK] -- by qa.views.handler')
