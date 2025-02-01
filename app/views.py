

from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from app.forms import CommentForm
from app.models import BlogPost
from form import ContactForm


def index(request):
    return render(request, 'index.html')


def blog(request):
    posts = BlogPost.objects.all()
    paginator = Paginator(posts, 6)  # Show 6 blog posts per page.
    page = request.GET.get('page')
    paginated_posts = paginator.get_page(page)
    context = {
        'posts': paginated_posts,
    }
    return render(request, 'blog.html', context)


def about(request):
    return render(request, 'about.html')


def class_(request):
    return render(request, 'class.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Optionally, you can add code here to send email notifications
            return redirect('index')  # Redirect to a success page or home page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


def feature(request):
    return render(request, "feature.html")


def single_view(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
    }
    return render(request, 'single.html', context)
