# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Book, Review
from ..logreg_app.models import User

def display(request):
    context = {
        'reviews' :Book.objects.all(),
        'another' :Review.objects.all()
    }
    return render(request, 'review_app/display.html', context)

def addbook(request):
    context = {
        'users' :User.objects.all(),
        'reviews' :Book.objects.all(),
        
    }
    return render(request, 'review_app/add.html', context)

def processing(request):
    user = User.objects.get(id=request.session['id'])
    # if 
    work = Book.objects.create(
        title = request.POST['title'],
        author = request.POST['custom_author'],
        user = user
        )
    id = work.id
    books = Book.objects.get(id=work.id)
    again = Review.objects.create(
        review = request.POST['review'],
        user = user,
        books = books
    )
    return redirect('/books/{}'.format(id))

def books(request, bookid):
    book = Book.objects.get(id=bookid)
    context = {
        'check' :book,
        'reviews': Review.objects.all()
    }
    return render(request, 'review_app/book.html', context)

def update(request, bookid):
    user = User.objects.get(id=request.session['id'])
    books = Book.objects.get(id=bookid)
    update = Review.objects.create(
        review = request.POST['newreview'],
        user = user,
        books = books
    )
    return redirect('/books/{}'.format(id))

def user(request, userid):
    user = User.objects.get(id=userid)
    context = {
        'reviews' : Review.objects.all()
    }
    return render(request, 'review_app/user.html', context)

def clear(request):
    request.session.flush()
    return redirect('/')