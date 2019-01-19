from django.shortcuts import render
from . models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404




# def posts_list(request):
#     """представление для просмотра списка всех постов с пагинатором"""
#
#     search_query = request.GET.get('search', '')  # проверяет по ключу search - ввел ли пользователь в поисковике слово
#
#     if search_query:  # если ввел
#         posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))  # возвращаем совпадение
#     else:
#         posts = Post.objects.all()  # иначе передаем дальше список постов
#
#     # пагинация
#     paginator = Paginator(posts, 2)
#     page_number = request.GET.get('page', 1)
#     page = paginator.get_page(page_number)
#     is_paginated = page.has_other_pages()
#
#     if page.has_previous():
#         prev_url = '?page={}'.format(page.previous_page_number())
#     else:
#         prev_url = ''
#
#     if page.has_next():
#         next_url = '?page={}'.format(page.next_page_number())
#     else:
#         next_url = ''
#
#     context = {
#         'page_object': page,
#         'is_paginated': is_paginated,
#         'next_url': next_url,
#         'prev_url': prev_url
#     }
#
#     return render(request, 'blog/index.html', context=context)

class PostListView(generic.ListView):
    model = Post
    paginate_by = 10


class PostDetailView(generic.DetailView):
    model = Post


class PostCreate(PermissionRequiredMixin, CreateView):
    model = Post
    fields = '__all__'
    # initial = {'summary': 'This book is...', }
    permission_required = ''


class PostUpdate(PermissionRequiredMixin, UpdateView):
    model = Post
    fields = '__all__'
    permission_required = ''


class PostDelete(PermissionRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('articles')
    permission_required = ''


class PostCommentCreate(LoginRequiredMixin, CreateView):
    """
    Form for adding a blog comment. Requires login.
    """
    model = PostComment
    fields = ['comment', ]

    def get_context_data(self, **kwargs):
        """
        Добавляет связанный блог в шаблон формы, чтобы его заголовок отображался в HTML.
        """
        # Call the base implementation first to get a context
        context = super(PostCommentCreate, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['post'] = get_object_or_404(Post, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        """
        Добавляет автора и связанный блог, чтобы сформировать данные,
        прежде чем задавать их действительными (чтобы они сохранялись в модели)
        """
        # Добавить зарегистрированного пользователя как автора комментария
        form.instance.author = self.request.user
        # Связать комментарий с блогом на основе переданного идентификатора
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        # Вызвать поведение проверки формы суперкласса
        return super(PostCommentCreate, self).form_valid(form)

    def get_slug_field(self):
        """Get the name of a slug field to be used to look up by slug."""
        return self.slug_field

    def get_success_url(self):
        """
        After posting comment return to associated blog.
        """
        post = Post.objects.get(pk=self.kwargs['pk'])
        print(post.slug)
        return reverse('post_detail', kwargs={'slug': post.slug, })
