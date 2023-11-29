from django.shortcuts import render, get_object_or_404
from .models import Post,Comment
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm,CommentForm, SearchForm
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank,TrigramSimilarity
from django.http import JsonResponse



def home_view(request):
    object_list=Post.published.all()
    latest_posts=object_list.order_by('-publish')[:7]        
    return render(request,'app/index.html',{'posts':object_list,'latest_posts':latest_posts})


def single_post_view(request,blog_id):
    post = get_object_or_404(Post.published, id=blog_id)
    if(request.method=="POST"):
        comment_form=CommentForm(request.POST)
        if(comment_form.is_valid()):
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            comment_form=CommentForm()
    else:
        comment_form=CommentForm()
    
    comments=post.comments.filter(active=True)
    return render(request,'app/view_bog.html',{'posts':post,'comment_form':comment_form,'comments':comments})


def share_post(request,post_id):
    post=get_object_or_404(Post,id=post_id,status='published')
    sent = False
    if(request.method=='POST'):
        form=EmailPostForm(request.POST)
        if(form.is_valid()):
            cd=form.cleaned_data
            post_url=request.build_absolute_uri(post.get_absolute_url())
            subject=f"{cd['name']} recommends you to read {post.title}"
            message=f"Read {post.title} at {post_url}\n \n{cd['name']}\'s comments: {cd['comments']}"
            sender_email = cd['email']

            send_mail(subject, message, sender_email, [cd['to']])
            # send_mail(subject, message, cd['email'], ['ceotecs22@gmail.com',])
            sent=True
    else:
        form=EmailPostForm()
    return render(request, 'app/share.html',{'post':post,'form':form,'sent':sent})



def post_search_view(request):
    query = request.GET.get('query', '') 
    if query == '':
        filtered_posts = Post.objects.all()
    else:
        filtered_posts = Post.objects.filter(title__icontains=query)
    posts_data = []  
    for post in filtered_posts:
        posts_data.append({
            'id': post.id,
            'title': post.title,
            'image': post.blog_image.url
        })

    return JsonResponse({'posts': posts_data})