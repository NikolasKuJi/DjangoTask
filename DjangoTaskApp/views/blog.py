from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views import View

from DjangoTaskApp.models import Post


class PostList(View):
    def get(self, request):
        context = {}
        posts = Post.objects.all().prefetch_related("comment_set")
        context["post_list"] = posts
        return render(request, "blog/post_list.dj.html", context)


class PostView(View):
    def get(self, request, post_id):
        context = {}
        try:
            post = Post.objects.get(id=post_id)
        except ObjectDoesNotExist:
            return HttpResponseNotFound("hello")
        context["post"] = post
        return render(request, "blog/post_view.dj.html", context)

