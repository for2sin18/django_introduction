from django.urls import path
from . import views
from cms.category_view import  CategoryView, CategoryEditView, CategoryDeleteView
from cms.post_view import PostView, PostEditView, PostDeleteView
from .link_view import LinkView
from.link_view import LinkEditView, LinkDeleteView
from .user_view import UserView
app_name = 'cms'
urlpatterns = [
    path('login/', views.cms_login, name='login'),
    path('dashboard/', views.cms_dashboard, name="dashboard"),
    path('dashboard/category/manage', views.category_manage_view, name="category_manage_view"),
    path('dashboard/category/publish', views.category_publish_view, name="category_publish_view"),
    path('dashboard/category/add', CategoryView.as_view(), name="category_add"),
    path('dashboard/category/edit', CategoryEditView.as_view(), name="category_edit_view"),
    path('dashboard/category/delete', CategoryDeleteView.as_view(), name="category_delete"),
    path('dashboard/post/manage', views.post_manage_view, name='post_manage_view'),
    path('dashboard/post/publish', views.post_publish_view, name='post_publish_view'),
    path('dashboard/post/add', PostView.as_view(), name="post_add"),
    path('dashboard/post/edit', PostEditView.as_view(), name='post_edit_view'),
    path('dashboard/post/delete', PostDeleteView.as_view(), name="post_delete"),
    path('dashboard/link/manage', views.link_manage_view, name="link_manage_view"),
    path('dashboard/link/publish', views.link_publish_view, name="link_publish_view"),
    path('dashboard/link/add', LinkView.as_view(), name="link_add"),
    path('dashboard/link/edit', LinkEditView.as_view(), name='link_edit_view'),
    path('dashboard/link/delete', LinkDeleteView.as_view(), name='link_delete'),
    path('dashboard/user/manage', views.user_manage_view, name="user_manage_view"),
    path('dashboard/user/publish', views.user_publish_view, name="user_publish_view"),
    path('dashboard/user/add', UserView.as_view(), name="user_add")


]