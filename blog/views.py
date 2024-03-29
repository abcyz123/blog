from django.shortcuts import render
from . import models

# Create your views here.


# 主页编写
def index(request):
    articles = models.Article.objects.all()
    return render(request, "index.html", {'articles': articles})


# 显示文章页面
def article_page(request, article_id):
    article = models.Article.objects.get(pk= article_id)
    return render(request, 'article_page.html', {'article': article})


# 新写博客和修改
def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'edit_page.html')
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'edit_page.html', {'article': article})


# 博客修改响应函数
def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    article_id = request.POST.get('article_id', '0')
    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, "index.html", {'articles': articles})
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'article_page.html', {'article': article})


# def edit_action(request):
#     title = request.POST.get('title', 'Title')
#     content = request.POST.get('content', 'Content')
#     models.Article.objects.create(title=title, content=content)
#     return HttpResponseRedirect(reverse('blog:index'))
