from rest_framework import serializers
from ..models import Bookmark, Category,Search
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class BookmarkSerializer(TaggitSerializer, serializers.ModelSerializer):

    tags = TagListSerializerField()
    
    category_name = serializers.CharField(source='category.name', read_only=True)
    
    author_name =serializers.CharField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Bookmark
        fields = ['id', 'author','author_name','title', 'url', 'ico',
                  'description', 'created','updated','is_public','is_valid','category','category_name','tags']


class CategorySerializer(serializers.ModelSerializer):
    coco = BookmarkSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'description','coco']

    def create(self, validated_data):
        cocos_data = validated_data.pop('coco')
        category = Category.objects.create(**validated_data)
        for coco_data in cocos_data:
            Bookmark.objects.create(category=category, **coco_data)
        return category

class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = ['name','description', 'url','q', 'icon']