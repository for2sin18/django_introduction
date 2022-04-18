from django import forms
from post.models import Category
from post.models import Post
from link.models import Link


class CategoryAddForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
class CategoryEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)
    class Meta:
        model = Category
        fields = "__all__"

# 如果想要通过后台管理系统来增加数据，我们需要django Form来处理前端的POST请求
class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('read_num',)
class PostEditForm(forms.ModelForm):
    pk = forms.CharField(max_length=100)
    class Meta:
        model = Post
        exclude = ('read_num',)

class LinkAddForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
class LinkEditForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = "__all__"


class UserAddForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(max_length=20, min_length=6, strip=True)

