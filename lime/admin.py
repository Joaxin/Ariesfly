from django.contrib import admin
from .models import Bookmark, Category, Search

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

    list_display = ('id','title', 'url', 'description', 'category','tag_list')
    list_filter = ('title', 'author', 'url', 'is_public',)
    search_fields = ('title', 'url',)
    date_hierarchy = 'pub_date'
    ordering = ('id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    ordering = ('name',)

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'q')
    ordering = ('name',)