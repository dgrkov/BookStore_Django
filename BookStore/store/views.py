from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.template import loader

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world. You're at the store index.")
    books_list = Book.objects.all()
    template = loader.get_template("books/index.html")
    context = {
        "books_list": books_list,
    }
    return HttpResponse(template.render(context, request))

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body><h1 align=center>It is now %s.</h1></body></html>" % now
    return HttpResponse(html)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/detail.html", {"book": book})


def author(request, auhtor_id):
    author = Author.objects.get(pk=auhtor_id)
    return render(request, "books/author.html", {"author": author})


def buy(request, book_id):
    return HttpResponse("You're buying book %s." % book_id)