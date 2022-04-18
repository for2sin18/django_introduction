from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from shortuuidfield import ShortUUIDField

class UserManager(BaseUserManager):
    def _create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError('Email required')
        if not username:
            raise ValueError('Username required')
        if not password:
            raise ValueError('password required')

        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, username, password, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **kwargs)

    def create_superuser(self, email, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(email, username, password, **kwargs)
    def create_staffuser(self, email, username, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **kwargs)

class User(AbstractBaseUser, PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    objects = UserManager()

# class Article(models.Model):
#     #文章的唯一ID
#     article_id = models.AutoField(primary_key=True)
#     #文章标题
#     title = models.TextField()
#     # #文章作者
#     author = models.ForeignKey('blog.User', on_delete=models.SET_NULL, null=True)
#     #文章摘要
#     brief_content = models.TextField()
#     #文章主要内容
#     content = models.TextField()
#     #文章的发布日期
#     publish_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title


