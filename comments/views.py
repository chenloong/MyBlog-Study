from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from Web.models import Article

from .models import Comment
from .forms import CommentForm


def article_comment(request, article_id):
    article_obj = get_object_or_404(Article, id = article_id)
    id = int(article_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article_obj
            comment.save()
            comment_list = article_obj.comment_set.all()
            context = {
                'article_obj': article_obj,
                'form': form,
                'comment_list': comment_list
            }
            # return render(request, "article.html", context=context)
            return HttpResponseRedirect("/article/%d/" %(id))
        else:
            comment_list = article_obj.comment_set.all()
            context = {
                'article_obj': article_obj,
                'form' : form,
                'comment_list': comment_list
            }
        return render(request, 'article.html', context=context)
    comment_list = Comment.objects.all()
    print "-->%s" % comment_list
    return render(request, 'article.html', {'comment_list':comment_list, 'acticle': article_obj})