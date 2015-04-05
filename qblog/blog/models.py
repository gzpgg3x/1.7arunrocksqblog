from django.db import models
from django.core.urlresolvers import reverse

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

# class Tag(models.Model):
#     slug = models.SlugField(max_length=200, unique=True)

#     def __str__(self):
#         return self.slug

#     def get_absolute_url(self):
#         return reverse("tag_detail", kwargs={"slug": self.slug}) 

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("tag_index", kwargs={"slug": self.slug})       

# class Entry(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     slug = models.SlugField(max_length=200,unique=True)
#     publish =  models.BooleanField(default=False)
#     created = models.DateTimeField(auto_now_add=True)
#     modified = models.DateTimeField(auto_now=True)
#     tags = models.ManyToManyField(Tag) 
    
#     objects = EntryQuerySet.as_manager()

#     def get_absolute_url(self):
#         # return reverse("entry_detail", kwargs={"slug": self.slug}) 
#         return reverse("entry_detail", kwargs={"slug": self.slug})           

#     def __str__(self):
#         # return self.entry_title
#         return self.title

#     class Meta:
#         verbose_name = "Blog Entry"
#         verbose_name_plural = "Blog Entries"
#         ordering = ['-created']

class Entry(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True, null=True)
    publish = models.BooleanField(default=False)
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag)

    objects = EntryQuerySet.as_manager()

    def save(self):
        self.body_html = markdown2.markdown(self.body, extras=['fenced-code-blocks'])
        super(Entry, self).save()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
        ordering = ['-created']      



        
