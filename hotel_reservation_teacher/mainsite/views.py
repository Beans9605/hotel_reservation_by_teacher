from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "mainsite/home.html")

def easy_booking(request):
    return render(request, "mainsite/home.html")


def about(request):
    return render(request, "about/about.html")