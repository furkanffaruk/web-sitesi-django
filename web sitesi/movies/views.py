from django.shortcuts import render
from .models import Category,Movie

def home(req):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(main=True)
    }

    return render(req,"home.html",data)


def movies(req):
    data = {
        "kategoriler":Category.objects.all(),
        "filmler" : Movie.objects.all()
    }
    return render(req,"movies.html",data)

def movie_details(req,id):
    data={
            "film": Movie.objects.get(id=id)
    }

    return render(req,"details.html",data)

def macera(req):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(macera=True)
    }

    return render(req,"movies.html",data)

def aksiyon(req):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(aksiyon=True)
    }

    return render(req,"movies.html",data)

def korku(req):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(korku=True)
    }

    return render(req,"movies.html",data)
def gerilim(req):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(gerilim=True)
    }

    return render(req,"movies.html",data)

def dram(req):
    data = {
        "kategoriler" : Category.objects.all(),
        "filmler" : Movie.objects.filter(dram=True)
    }

    return render(req,"movies.html",data)