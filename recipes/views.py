from django.shortcuts import render
# from django.http import HttpResponse


def show_recipe(request):
    return render(request, "recipes/detail.html")
