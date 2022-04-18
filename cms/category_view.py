from django.views.generic import View
from django.urls import reverse
from django.shortcuts import redirect, render
from cms.forms import CategoryAddForm, CategoryEditForm
from post.models import Category
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator # 添加一个装饰器到类内部的方法

@method_decorator(login_required, name='post')
class CategoryView(View):
    def post(self, request):
        # 新建提交
        if 'submit' in request.POST:
            form = CategoryAddForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data.get('name')
                Category.objects.create(name=name)
                return redirect(reverse('cms:category_manage_view'))
            else:
                print("Form has error:{}".format(form.get_errors()))
                return redirect(reverse('cms:category_publish_view'))
        # 修改Category
        elif 'modify' in request.POST:
            form = CategoryEditForm(request.POST)
            if form.is_valid():
                pk = form.cleaned_data.get('pk')
                name = form.cleaned_data.get('name')
                Category.objects.filter(id=pk).update(name=name)
                return redirect(reverse("cms:category_manage_view"))
            else:
                return redirect(reverse("cms:category_manage_view"))
        # 修改状态的 返回
        elif 'back':
            return redirect(reverse("cms:category_manage_view"))
        # 新建状态的 取消
        else:
            return redirect(reverse('cms:category_manage_view'))
@method_decorator(login_required, name='get')
class CategoryEditView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        category = Category.objects.get(pk=category_id)
        context = {
            'item_data': category
        }
        return render(request, 'cms/category/publish.html', context=context)
@method_decorator(login_required, name='get')
class CategoryDeleteView(View):
    def get(self, request):
        category_id = request.GET.get('category_id')
        Category.objects.filter(id=category_id).delete()
        return redirect('cms:category_manage_view')
