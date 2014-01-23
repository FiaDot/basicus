from django.test import TestCase
#from django.utils import unittest

from board.models import Categories
from board.models import Article


class ArticleModelTestCase(TestCase):
    def setUp(self):
        category = Categories.objects.create(Title='general')
        Article.objects.create(Title="unittest", Body="empty body", Category=category)
        
    def test_article_model(self):
        article = Article.objects.get(Title="unittest")
        self.assertEqual('unittest', article.Title)
        
#    def test_only_false(self):
#        self.assertFalse(True)        
