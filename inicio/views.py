from django.shortcuts import render


def mostrarInicio(request):
    return render(request, "inicio.html")
