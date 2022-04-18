from django.urls import path
import blog.views
from django.conf.urls.static import static
from django.conf import settings
app_name = 'blog'
urlpatterns=[
    # path('content', blog.views.article_content),
    # path('base', blog.views.get_index_page),
    # #path('detail',blog.views.get_detail_page),
    # path('detail/<int:article_id>', blog.views.get_detail_page),
    path('login/', blog.views.login_view, name="login"),
    path('logout/', blog.views.logout_view, name='logout'),
]

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)