from django.shortcuts import render

def index_main(request):
    return render(request, 'index.html', context={'page':''})