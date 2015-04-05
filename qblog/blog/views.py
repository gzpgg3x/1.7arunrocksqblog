from django.shortcuts import render
from django.views import generic
from . import models
from models import Entry

class BlogIndex(generic.ListView):
    # queryset = models.Entry.objects.published()
    queryset = models.Entry.objects.all()    
    template_name = "blog/home.html"
    paginate_by = 2

class BlogDetail(generic.DetailView):
    model = Entry
    # template_name = 'blog/detail.html'
    template_name = 'blog/post.html'

    # def get_queryset(self):
    #     return Entry.objects.all()