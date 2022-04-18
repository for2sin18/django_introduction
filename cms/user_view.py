from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import View

from blog.models import User
from cms.forms import UserAddForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from blog.decorator import luc_login_superuser_required

@method_decorator(login_required, name="post")
@method_decorator(luc_login_superuser_required, name='post')
class UserView(View):
    def post(self, request):
        # 新建提交
        if 'submit' in request.POST:
            form =UserAddForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                User.objects.create_staffuser(email=email, username=username, password=password)
                return redirect(reverse('cms:user_manage_view'))
            else:
                return redirect(reverse('cms:user_publish_view'))

        else:
            return redirect(reverse("cms:user_publish_view"))
