from django.shortcuts import render

# Create your views here.


def menu(request):
    context = {"section": "menu"}

    return render(request, "menu/menu.html", context=context)
