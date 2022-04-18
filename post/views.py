from django.shortcuts import render
from post.models import Post
# Create your views here.
from django.shortcuts import render
import markdown
from link.models import Link


def index(request):
    top_post = Post.objects.filter(status=Post.STATUS_NORMAL, priority__gt=0).order_by('-priority')
    if len(top_post) > 4:
        top_post = top_post[:4]
    list_post = Post.objects.filter(status=Post.STATUS_NORMAL, priority=0)
    context = {
            'top_post': top_post,
            'list_post': list_post
        }
    context.update(get_read_most_post())
    context.update(get_link())
    return render(request, 'post/index.html', context=context)
# 实现首页的文章列表页
def post_list_view(request):
    hot_post = Post.objects.filter(status=Post.STATUS_NORMAL, is_hot=True).order_by('time_id')
    list_post = Post.objects.filter(status=Post.STATUS_NORMAL, is_hot=False).order_by('time_id')
    context = {
        'hot_post': hot_post,
        'list_post': list_post,
    }
    context.update(get_read_most_post())
    context.update(get_link())
    return render(request, 'post/list.html', context=context)
# 文章详情页视图函数
def detail(request, time_id):
    post = Post.objects.select_related('category', 'author').get(time_id=time_id)
    md = markdown.Markdown(
        extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ]
    )
    md.convert(post.content)
    context = {
        'post_data': post,
        'toc': process_toc(md.toc)
    }
    context.update(get_read_most_post())
    context.update(get_link())
    return render(request, 'post/detail.html', context=context)
# 读取右边栏阅读排行榜数据
def get_read_most_post():
    read_post = Post.objects.all().order_by('-read_num')
    if len(read_post) > 5:
        read_post = read_post[:5]
    context = {
        'read_post': read_post
    }
    return context
def process_toc(toc):
    toc = toc.replace('<div class="toc">', '').replace('</div>', '').replace('<ul>', '<ul class="list-group">').replace('<li>', '<li class="border-0 list-group-item">')
    if len(toc) <= 31:
        toc = None
    return toc
def get_link():
    links = Link.objects.filter(status=Link.STATUS_NORMAL)
    context = {
        'link_data': links
    }
    return context