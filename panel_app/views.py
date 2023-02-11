from django.shortcuts import render


def index(request):
    context={}
    return render(request,'pages/index.html',context)


def books(request):
    context={}
    return render(request,'pages/books.html',context)


def delete(request):
    context={}
    return render(request,'pages/delete.html',context)


def update(request):
    context={}
    return render(request,'pages/update.html',context)