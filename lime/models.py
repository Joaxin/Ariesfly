from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager

User = settings.AUTH_USER_MODEL

class PublicManager(models.Manager):
    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(is_public='true')

class Search(models.Model):

    name = models.CharField('name', max_length=255)
    description = models.TextField('description', blank=True)
    url = models.URLField()
    q = models.CharField('keywords', max_length=10)
    icon = models.ImageField(upload_to='search/', blank=True)

    class Meta:
        verbose_name = 'serach'
        verbose_name_plural = verbose_name
        ordering = ['name']

    def __str__(self):
        return '%s (%s)' % (self.name, self.url)

class Category(models.Model):

    name = models.CharField(verbose_name='分类', max_length=20)
    description = models.TextField('description', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def __str__(self):
         return '%s (%s)' % (self.name, self.description)

class Bookmark(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='author')
    url = models.URLField()
    ico = models.ImageField(upload_to='user/b%Y/', blank=True)
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    is_valid= models.BooleanField('valid', default=True)

    created = models.DateTimeField('date created',auto_now_add=True)
    updated = models.DateTimeField('date updated',auto_now=True)
    pub_date = models.DateField('date published', default=timezone.now)

    category = models.ForeignKey(Category, related_name='coco',on_delete=models.CASCADE)
    tags=TaggableManager()

    objects = models.Manager()
    public = PublicManager()

    class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['category','id']

    def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
