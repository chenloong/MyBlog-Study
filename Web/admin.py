#coding:utf-8
from django.contrib import admin
import models

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'head_img', 'author', 'publish_date', 'hidden', 'Priority')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'article', 'user', 'parent_comment', 'comment')


class ThumbUPAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date')

admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
# admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.ThumbUP, ThumbUPAdmin)
admin.site.register(models.UserProfile)
admin.site.register(models.UserGroup)