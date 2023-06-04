from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView, CreateView

from common.views import TitleMixin
from posts.forms import PostCreateForm, CommentForm
from posts.models import Post, Like


class PostListView(TitleMixin, ListView):
    template_name = 'posts/list.html'
    model = Post
    context_object_name = 'posts'
    title = 'Главная'
    paginate_by = 5


class PostDetail(FormMixin, DetailView):
    model = Post
    template_name = 'posts/detail.html'
    pk_url_kwarg = 'pk'
    context_object_name = 'post'
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('posts:detail', kwargs={'pk': self.get_object().id})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        object.post = self.get_object()
        object.save()
        return super().form_valid(form)


@login_required
def like(request, pk):
    post = Post.objects.get(pk=pk)
    user = request.user
    if not Like.objects.filter(post=post, user=user).exists():
        liked = Like(post=post, user=user)
        liked.save()
    else:
        liked = Like.objects.filter(post=post, user=user)
        liked.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class PostCreateView(TitleMixin, CreateView):
    template_name = 'posts/create.html'
    model = Post
    form_class = PostCreateForm
    title = 'Создать пост'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
