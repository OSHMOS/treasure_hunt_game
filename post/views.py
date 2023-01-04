from django.shortcuts import render, reverse
from .models import Post
from .forms import PostForm
from django.views.generic import CreateView
# Create your views here.


def greeting(request):
    return render(request, 'greeting.html')


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/post_form.html"

    def get_success_url(self):
        return reverse('greeting')


def create(request):
    if request.method == 'POST':
        pass
    else:
        post = PostForm()
    return render('post/create_form.html')
