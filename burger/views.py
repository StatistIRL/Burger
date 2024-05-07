from django.shortcuts import render

# Create your views here.


def main_page(request):

    context = {"section": "main"}
    return render(request, "burger/index.html", context=context)
