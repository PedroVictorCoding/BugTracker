from django.shortcuts import render

def home_view(request):
    args = {}
    return render(request, 'home/index.html', args)
