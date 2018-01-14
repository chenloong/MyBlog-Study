#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
import os

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5)
    category_id = forms.IntegerField()
    # summary = forms.CharField(max_length=255, min_length=5)
    head_img = forms.ImageField()
    content = forms.CharField(min_length=10)

def handle_upload_file(request, f):
    base_img_upload_path = "static/images"
    user_path = "%s/%s" %(base_img_upload_path, request.user.userprofile.id)
    if not os.path.exists(user_path):
        os.mkdir(user_path)
    with open("%s/%s" %(user_path, f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return "/static/images/%s/%s" %(request.user.userprofile.id, f.name)


# 用户注册