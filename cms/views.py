from django.shortcuts import render
from post.models import Category, Post
from blog.models import User
from tools.paginator_helper import get_pagiator, get_pagination_data
from link.models import Link
from django.contrib.auth.decorators import login_required
from blog.decorator import luc_login_superuser_required
# Create your views here.
def cms_login(request):
    return render(request, 'cms/login.html')
@login_required
def cms_dashboard(request):
    return render(request, 'cms/dashboard/home.html')
@login_required
def category_manage_view(request):
    context = {
        "list_data": Category.objects.all()
    }
    return render(request, 'cms/category/manage.html', context=context)
@login_required
def category_publish_view(request):
    return render(request, 'cms/category/publish.html')

@login_required
def post_manage_view(request):
    page = int(request.GET.get('p', 1))
    posts = Post.objects.all()
    paginator = get_pagiator(posts)
    page_obj = paginator.page(page)
    context = {
        'list_data': page_obj.object_list,
        'list_data_status': Post.STATUS_ITEMS # 添加Post Status状态
    }
    context.update(get_pagination_data(paginator, page_obj))
    return render(request, 'cms/post/manage.html', context=context)
@login_required
def post_publish_view(request):
    context = {
        'list_data_category':Category.objects.all(),
        'list_data_user': User.objects.all(),
        'list_data_status': Post.STATUS_ITEMS
    }
    return render(request, 'cms/post/publish.html', context=context)
@login_required
def link_manage_view(request):
    context = {
        'list_data': Link.objects.all(),
        'list_data_status': Link.STATUS_ITEMS
    }
    return render(request, 'cms/link/manage.html', context=context)
@login_required
def link_publish_view(request):
    context = {
        'list_data_status': Link.STATUS_ITEMS
    }
    return render(request, 'cms/link/publish.html', context=context)

@login_required
@luc_login_superuser_required
def user_manage_view(request):
    context = {
        'list_data': User.objects.all()
    }
    return render(request, 'cms/user/manage.html', context=context)

@login_required
@luc_login_superuser_required
def user_publish_view(request):
    return render(request, 'cms/user/publish.html')