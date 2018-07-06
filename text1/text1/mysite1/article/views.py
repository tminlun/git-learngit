from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from .models import Article

# Create your views here.


def article_detail(request,article_id):
    article = get_object_or_404(Article,id=article_id)
    context = {}
    context['article_obj'] = article
    return render_to_response("article_detail.html",context)
    # except Article.DoesNotExist:
    #     raise Http404("not exise")
    # return HttpResponse("<h1>文章标题: %s</h1> 文章内容: %s" % (article.title, article.content))

def article_list(request):
    articles = Article.objects.all()#获取所有文章列表，文章对象
    #获取文章页面
    context = {}
    context['articles'] = articles
    return render_to_response("article_list.html",context)