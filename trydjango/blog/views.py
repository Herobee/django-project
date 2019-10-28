from django.shortcuts import render

from django.views.generic import(
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView
)
from .models import Article

class ArticleListView(ListView):
    queryset = Article.objects.all()
