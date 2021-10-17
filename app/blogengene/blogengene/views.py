from django.shortcuts import render

def hi(request):
    return render(request, 'index.html', context={'alert':'alert_style'})