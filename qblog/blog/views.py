from django.shortcuts import render
from django.views import generic
from . import models
from models import Entry, Tag

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

# class TagIndex(generic.ListView):
#     template = 'home.html'
#     paginate_by = 5

#     def get_queryset(self):
#         slug = self.kwargs['slug']
#         tag = Tag.objects.get(slug=slug)
#         results = Entry.objects.filter(tags=tags)
#         return results

class TagIndex(generic.ListView):
    template_name = 'blog/home.html'
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['slug']
        tag = Tag.objects.get(slug=slug)
        results = Entry.objects.filter(tags=tag)
        return results