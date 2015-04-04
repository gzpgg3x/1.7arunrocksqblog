from django.shortcuts import render
from django.views import generic
from . import models

class BlogIndex(generic.ListView):
    # queryset = models.Entry.objects.published()
    queryset = models.Entry.objects.all()    
    template_name = "blog/home.html"
    paginate_by = 2