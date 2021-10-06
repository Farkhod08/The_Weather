from django.shortcuts import render


def MainHome(request):
    return render(request, template_name='MainHome.html')
