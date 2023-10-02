from django.urls import path

from DjangoTaskApp.views.blog import PostList, PostView

djangotaskapp_patterns = ((
    path('', PostList.as_view(), name="index"),
    path('<int:post_id>/', PostView.as_view(), name="post")
), "djangotaskapp")
