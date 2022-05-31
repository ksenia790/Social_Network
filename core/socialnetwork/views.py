from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from comments.forms import CommentForm
from comments.models import Comment


def post_list(request):
    '''
    Returns all published posts.
    '''

    posts = Post.published.all()
    return render(request,'post_list.html',{'posts':posts, page:'pages'})


def post_detail(request, post):
    ''' 
    Returns particular published post by it's slug-name. 
    '''

    post = get_object_or_404(Post,slug=post,status='published')
    comments = post.comments.filter(active=True)
    new_comment = None
    comment_form = CommentForm(data=request.POST) 
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return redirect(post.get_absolute_url()+'#'+str(new_comment.id))
        else:
            comment_form = CommentForm()
 

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
    return redirect("")
