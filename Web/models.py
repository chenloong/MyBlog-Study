#coding:utf-8


from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# 帖子表
class Article(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name=u"文章标题")
    category = models.ForeignKey("Category", verbose_name=u"版块")
    head_img = models.ImageField(upload_to="static/images")
    summary = models.CharField(max_length=255, verbose_name=u"概述")
    content = models.TextField(verbose_name=u"内容")
    author = models.ForeignKey("UserProfile", verbose_name=u"作者")
    publish_date = models.DateTimeField(auto_now=True, verbose_name=u"发布日期")
    views = models.PositiveIntegerField(default=0, verbose_name=u"浏览量")
    hidden = models.BooleanField(default=False, verbose_name=u"隐藏")
    Priority = models.IntegerField(default=1000, verbose_name=u"优先级")

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    def save(self, *args, **kwargs):
        self.summary = self.content[:54]
        super(Article, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s, author:%s" %(self.title, self.author)


# 评论表
class Comment(models.Model):
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    parent_comment = models.ForeignKey("self", related_name="p_comment", blank=True, null=True)
    comment = models.TextField(max_length=1000)

    def __unicode__(self):
        return "%s, user:%s" %(self.article, self.user)


# 点赞表
class ThumbUP(models.Model):
    article = models.ForeignKey("Article")
    user = models.ForeignKey("UserProfile")
    date = models.DateField(auto_now=True)


# 版块表
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)
    admin = models.ManyToManyField("UserProfile", verbose_name=u"管理员")

    def __unicode__(self):
        return self.name


# 用户信息表
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=12)
    group = models.ManyToManyField("UserGroup")

    def __unicode__(self):
        return self.name


# 用户组表
class UserGroup(models.Model):
    name = models.CharField(max_length=32, unique=True)

    def __unicode__(self):
        return self.name