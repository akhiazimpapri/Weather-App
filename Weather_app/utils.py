from django.shortcuts import render


def searchCity(request):
    city = "Dhaka"
    if request.method == "POST":
        city = request.POST["city"]
    return city
