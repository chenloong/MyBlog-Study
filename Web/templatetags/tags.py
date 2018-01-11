#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Web.models import Article, Category
from django import template

'''
这里我们首先导入 template 这个模块
然后实例化了一个 template.Library 类，并将函数 get_newest_article 装饰为 register.simple_tag。
确保在使用模板标签以前导入了 tags，即 {% load tags %}。注意要在使用任何 tags 下的模板标签以前导入它。
这样就可以在模板中使用语法 {% get_newest_article %} 调用这个函数了。
'''
register = template.Library()

# 最新文章模板标签
# 获取数据库中前 num 篇文章，这里 num 默认为 5。
@register.simple_tag
def get_newest_article(num=5):
    return Article.objects.all().order_by('-publish_date')[:num]


# 归档模板标签
# 这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Article）的创建时间，且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义，一个是 publish_date ，即 Article 的创建时间，month 是精度，order='DESC' 表明降序排列（即离当前越近的时间越排在前面）。
@register.simple_tag
def archives():
    return Article.objects.datetimes('publish_date', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    return Category.objects.all()
