from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect

from .models import Post
from .forms import PostForm

def new_post(request):
    print("Inside request")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.title = "forum-message"
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post_list.html', {'posts':posts})


def post_list(request):
    print("Hey world")
    if request.method == "POST":
        print("sending request")
        post_new(request)
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'forum/post_list.html', {'posts':posts})

def send_message(request):
    print(request.POST['message'])
