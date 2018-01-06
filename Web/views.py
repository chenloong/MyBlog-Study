#coding:utf-8
from django.shortcuts import render, redirect, HttpResponseRedirect
from Web import models
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from .forms import ArticleForm, handle_upload_file
# Create your views here.


def index(request):
    Articles = models.Article.objects.all()
    return render(request, "index.html", {'Articles':Articles})


def category(request, category_id):
    Articles = models.Article.objects.filter(category_id=category_id)
    return render(request, 'index.html', {'Articles':Articles})


def article_ditail(request, article_id):
    try:
        article_obj = models.Article.objects.get(id=article_id)

        # 阅读量 +1
        article_obj.increase_views()

    except ObjectDoesNotExist as e:
        return render(request, '404.html', {'err_msg':u"文章不存在!"})
    return render(request, "article.html", {'article_obj':article_obj})


def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def acc_login(request):
    err_msg = ""
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            err_msg = u"用户名或密码错误!"
    return render(request, 'login.html', {'err_msg': err_msg})


def new_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['author_id'] = request.user.userprofile.id
            new_img_path = handle_upload_file(request, request.FILES['head_img'])
            form_data['head_img'] = new_img_path
            new_article_obj = models.Article(**form_data)
            new_article_obj.save()
            return render(request, 'new_article.html', {'new_article_obj': new_article_obj})
    category_list = models.Category.objects.all()
    return render(request, 'new_article.html', {'category_list':category_list})


def register(request):
    errors = []
    username = None
    password = None
    password2 = None
    email = None
    CompareFlag = False

    if request.method == "POST":
        if not request.POST.get('username'):
            errors.append(u'请输入用户名')
        else:
            username = request.POST.get('username')
        if not request.POST.get('password'):
            errors.append(u'请输入密码')
        else:
            password = request.POST.get('password')
        if not request.POST.get('password2'):
            errors.append(u'请重复输入密码')
        else:
            password2 = request.POST.get('password2')
        if not request.POST.get('email'):
            errors.append(u'请输入email')
        else:
            email = request.POST.get('email')

        if password is not None and password2 is not None:
            if password == password2:
                CompareFlag = True
            else:
                errors.append(u'两次输入的密码不同，请重新输入')

        if username is not None and password is not None and password2 is not None and email is not None and CompareFlag:
            user = User.objects.create_user(username, email, password )
            user.is_active = True
            user.save
            return HttpResponseRedirect('/')

    return render(request, 'register.html', {'errors':errors})