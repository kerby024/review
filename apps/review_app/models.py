# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..logreg_app.models import User
from django.db import models

class BookManager(models.Manager):

    def addreview(self, userid, bookid):
        f1 = User.objects.get(id = userid)
        f2 = Book.objects.get(id = bookid)
        f2.user.add(f1)
        f2.save()

    def removefavorites(self, userid, itemid):
        f1 = User.objects.get(id = userid)
        f2 = Book.objects.get(id = itemid)
        f2.favorited.remove(f1)
        f2.save()

class Book(models.Model):
    user = models.ForeignKey(User, related_name='people')
    title= models.CharField(max_length = 255)
    author = models.CharField(max_length = 255, unique=True)
    objects = BookManager()

class Review(models.Model):
    review = models.TextField(max_length = 1000)
    books = models.ForeignKey(Book, related_name='stories')
    user = models.ForeignKey(User, related_name='names')
    likes = models.ManyToManyField(User, related_name='liked')
    objects = BookManager()