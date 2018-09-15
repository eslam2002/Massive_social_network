from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *
from accounts.models import *
from django.contrib.auth import get_user_model
from django.db.models import Q

from django.urls import reverse_lazy
from django.views.generic import (CreateView,ListView,
                                UpdateView,DeleteView,
                                DetailView)

User = get_user_model()


class PostCreatView(CreateView,LoginRequiredMixin):
    model = Post
    # fields = ('content',)
    form_class = PostModelForm
    template_name = 'posts/create_post.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        # connect the post to the user
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    queryset = Post.objects.all()
    form_class = PostModelForm
    template_name = 'posts/update_post.html'
    #success_url = "/tweet/"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'posts/delete_confirm.html'
    success_url = reverse_lazy("posts:list") #reverse()

#
#
# class PostDetailView(DetailView):
#     queryset = Post.objects.all()


class PostListView(ListView):

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                    )
        return qs


    model = Post
    template_name = 'posts/list_post.html'
    context_object_name = 'post_list'

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = PostModelForm()
        context['create_url'] = reverse_lazy("post:create")
        return context



class UserDetailView(DetailView):
    template_name = 'posts/user_detail.html'
    queryset = User.objects.all()
    def get_object(self):
        return get_object_or_404(
                    User,
                    username__iexact=self.kwargs.get("username")
                    )

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        return context
