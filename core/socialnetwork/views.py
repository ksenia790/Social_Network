from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect


def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.slug = slugify(post.title)
            data.user = request.username
            data.save()
            return redirect("/")
    return render(request, "add_post.html", {"form": form})


#class CreatePost(CreateView):
 #   model = Post
  #  template_name = 'add_post.html'
   # fields = '__all__'
    #fields = ['title', 'slug', 'author', 'body', 'image', 'status']


def post_list(request):
    '''
    Returns all published posts.
    '''

    posts = Post.published.all()
    return render(request,'post_list.html',{'posts':posts})


def post_detail(request, post):
    ''' 
    Returns particular published post by it's slug-name. 
    '''

    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm(data=request.POST)
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url()) #+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()
    return render(request, 'post_detail.html',{'post':post,'comments':comments,'comment_form':comment_form, "is_liked": is_liked, "total_likes": post.total_likes(), "total_dislikes": post.total_dislikes()})


def like_post(request):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())


def reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('post_id') 
            parent_id = request.POST.get('parent') 
            post_url = request.POST.get('post_url')
            reply = form.save(commit=False)
            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.children = Comment(id=parent_id)
            reply.save()
            return redirect(post_url+'#'+str(reply.id))
    return redirect("/")
