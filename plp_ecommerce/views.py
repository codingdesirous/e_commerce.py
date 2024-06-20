from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>My first webpage with python</h1>"),