from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Followers


# Create your views here.
def home(request, yosh):
    return render(request, "index.html", {'yosh': yosh})


def sayt(request):
    return HttpResponse("<h3>MY first project of Django</h3>")


# yosh bu -> path parametr
def permission(request, yosh):
    if yosh > 18:
        return HttpResponse("<h1>Sizga kirish mumkin :</h1>")
    else:
        return HttpResponse("<h1>Siz hali voyaga yetmagansz</h1>")


def inform(request, familiya, ism):
    return HttpResponse(f"<h1>Sizning ismingiz: {ism}</h1>"
                        f"<h1>sizning familiyangiz: {familiya}</h1>")


def register(request):
    print(request)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        print(full_name)
        return redirect("/")
    return render(request, "register.html")


def index(request):
    print(request)
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        print(full_name)
        return redirect("/")
    return render(request, "index.html")


def git_copy(request):
    print(request)
    if request.method == "POST":
        print(request.POST)
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        if Followers.objects.filter(email=email).exists():
            return HttpResponse("BU EMAIL orqali oldin royxatdan otilgan ")

        Followers.objects.create(
            full_name=full_name,
            email=email,
            password=password,
            password1=password1
        )
        return redirect("/")
    return render(request, "git_copy.html")
