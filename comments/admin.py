from django.contrib import admin
import models

# Register your models here.

class CommentAdnin(admin.ModelAdmin):
    list_display = ('name', 'email', 'url', 'text', 'created_time', 'article')


admin.site.register(models.Comment, CommentAdnin)