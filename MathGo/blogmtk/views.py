from django.shortcuts import render

# Create your views here.
def awal(request):
    return render(request, 'base.html',)

def tengah(request):
    return render(request, 'math.html',)

def akhir(request):
    return render(request, 'fact.html',)
