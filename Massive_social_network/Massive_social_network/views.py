from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import render
from django.views import View
from posts.models import Post

User = get_user_model()

class SearchView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get("q")
        posts = Q(content__icontains=query)
        users = Q(username__icontains=query)
        qsUsers = None
        qsPosts = None
        if query:                                          #|
            qsUsers = User.objects.filter(
                 users
                )
            qsPosts = Post.objects.filter(
                posts
                )
        context = {"users": qsUsers,"posts":qsPosts}
        return render(request, "posts/search.html", context)
