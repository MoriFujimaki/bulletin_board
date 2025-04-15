from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Thread, Post
from .forms import ThreadForm, PostForm, SearchForm
from .forms import SearchForm
from django.contrib.auth.decorators import login_required
def thread_list(request):
    print('メインぺージを読み込むだなも！')
    message = "たぬきちの掲示板へようこそだなも！"
    print(message)
    threads = Thread.objects.all().order_by('-created_at')
    return render(request, 'board/thread_list.html', {'threads': threads, 'message': message})

def hello(request):
    return HttpResponse("たぬきちのHello Worldだなも！")
def tanukiti(request):
    return HttpResponse("まなはたぬきちだなも")

def thread_create(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save()
            return redirect('board:thread_detail', thread_id=thread.id)
    else:
        form = ThreadForm()
    return render(request, 'board/thread_create.html', {'form': form})

def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = Post.objects.filter(thread=thread).order_by('created_at')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.author = request.user if request.user.is_authenticated else None
            post.save()
            return redirect('board:thread_detail', thread_id=thread.id)
    else:
        form = PostForm()
    return render(request, 'board/thread_detail.html', {
        'thread': thread,
        'posts': posts,
        'form': form,
        
    })
def search(request):
    form = SearchForm(request.GET)
    threads = Thread.objects.all()
    posts = Post.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            # スレッドタイトルと投稿内容を検索
            threads = threads.filter(title__icontains=query)
            posts = posts.filter(content__icontains=query)
    return render(request, 'board/search_results.html', {'form': form, 'threads': threads, 'posts': posts})
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # 投稿者だけが削除できるようにする
    if request.user != post.author:
        return HttpResponseForbidden("あなたには削除権限がありません。")

    thread_id = post.thread.id  # 削除後にスレッド詳細に戻る用
    post.delete()
    return redirect('thread_detail', thread_id=thread_id)
def index(request):
    threads = Thread.objects.all().order_by('-created_at')
    return render(request, 'board/index.html', {'threads': threads})

def search_results(request):
     return redirect('board/search_results.html')