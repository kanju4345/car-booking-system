from django.shortcuts import render
def homes(request):
    return render(request, "booking/homes.html")


def about(request):
    return render(request, "booking/about.html")


def cars(request):
    return render(request, "booking/cars.html")


def contact(request):
    return render(request, "booking/contact.html")

def login(request):
    return render(request, "booking/login.html")
