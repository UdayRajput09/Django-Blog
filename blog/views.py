from django.shortcuts import render , get_object_or_404 , redirect 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post 
from .forms import PostForm , CommentForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def home(request):
    query = request.GET.get('q')

    if query:
        post_list = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        ).order_by('-created_at')
    else:
        post_list = Post.objects.all().order_by('-created_at')

    paginator = Paginator(post_list, 6)  
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/home.html', {'posts': posts})



def about(request):
    return render(request, 'blog/about.html')


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all().order_by('-created_at')

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post,
            'comments': comments,
            'form': form
        }
    )



@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request , "Post Created Successfully!")
            return redirect('home')
    else:
        form = PostForm()

    return render(request , 'blog/create_post.html' , { 'form' : form})
 

@login_required
def edit_post(request , slug):
    post = get_object_or_404(Post , slug = slug)

    if post.author != request.user:
        return redirect('home')
    
    if request.method == 'POST':
        form = PostForm(request.POST , instance=post)
        if form.is_valid():
            form.save()
            messages.success(request , "Post Updated Successfully!")
            return redirect('post_detail' , slug=post.slug)
        
    else:
        form = PostForm(instance=post)
    
    return render(request , 'blog/edit_post.html' , {'form' : form , 'post' : post}) 



@login_required
def delete_post(request , slug):
    post = get_object_or_404(Post , slug = slug)

    if post.author != request.user:
        return redirect('home')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request , "Post Deleted Successfully!")
        return redirect('home')
    
    return render(request , 'blog/delete_post.html' , { 'post' : post} )




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request ,user)
            messages.success(request , "Account Created Successfully!")
            return redirect('home')
    else:
        form = UserCreationForm()


    return render(request , 'registration/signup.html' , {'form' : form})



def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-created_at')

    return render( request,'blog/profile.html', {'profile_user': user,'posts': posts})



def toggle_like(request , slug):
    post = get_object_or_404(Post , slug = slug)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('post_detail' , slug =post.slug)
    