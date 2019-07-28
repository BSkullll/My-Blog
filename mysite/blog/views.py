from django.shortcuts import render
from blog.models import Post
from django.shortcuts import get_object_or_404
from blog.forms import PostForm

from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
	data = {
		'posts' : posts
		}
	return render(request, 'blog/post_list.html', context=data)

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	data = {'post':post}
	return render(request, 'blog/post_detail.html', context=data)

@login_required
def post_new(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	data = {'form':form}
	return render(request, 'blog/post_new.html', context=data)

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm(instance=post)

	data = {'form':form}
	return render(request, 'blog/post_new.html', context=data)

def about(request):
	return render(request, 'blog/about.html')