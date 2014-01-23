from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from board.models import Categories
from board.models import Article
from board.models import Comments


import logging

logger = logging.getLogger(__name__)


def board(request):
    logger.info('board')
    return HttpResponseNotFound('<h1>board</h1>')


def listpage(request, pk):
    logger.info('listpage')
    return HttpResponseNotFound('<h1>listpage</h1>')


def article(request, pk):
    return HttpResponseNotFound('<h1>article</h1>')


def write(request):
    return HttpResponseNotFound('<h1>write</h1>')


def comment(request, pk):
    return HttpResponseNotFound('<h1>comment</h1>')

