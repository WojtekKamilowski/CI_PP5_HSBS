# 3rd Part imports
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Internal imports
from profiles.models import UserProfile
from .models import Post, Comment
from .forms import PostForm, CommentForm


class Posts(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 4

    @login_required
    def add_post(request):
        """
        Displays form to create a new post
        """
        if not request.user.is_superuser:
            messages.error(
                request, 'Sorry, it is restricted option for store administration.')
            return redirect(reverse('home'))

        form = PostForm(data=request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "Post added!")
            return redirect("blog")

        return render(request, "blog/add_post.html", {"form": form})

    @login_required
    def edit_post(request, slug):
        """
        View to edit post
        """
        if not request.user.is_superuser:
            messages.error(
                request, 'Sorry, it is restricted option for store administration.')
            return redirect(reverse('home'))

        post = get_object_or_404(Post, slug=slug)
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "Post edit completed!")
                return redirect("blog")
        form = PostForm(request.POST, instance=post)
        context = {"form": form}
        return render(request, "blog/edit_post.html", context)

    @login_required
    def delete_post(request, slug):
        """
        Deletes post with option to confirm
        """
        if not request.user.is_superuser:
            messages.error(
                request, 'Sorry, it is restricted option for store administration.')
            return redirect(reverse('home'))

        post = get_object_or_404(Post, slug=slug)
        if request.method == "POST":
            post.delete()
            messages.success(request, "Post has been deleted!")
            return redirect("blog")
        return render(request, "blog/delete_post.html",
                      {"post": post})


class PostDetail(View):
    """
    Returns post details page
    """

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        Posts comment
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("-created_on")
        username = request.user
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.username = request.user.userprofile
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request,
                             'Your comment has been posted')
        else:
            comment_form = CommentForm()
            messages.warning(request,
                             'An error occurred. Please Try Again')

        template = "blog/post_detail.html"
        context = {
            "post": post,
            "comments": comments,
            "liked": liked,
            "comment_form": CommentForm(),
            "username": username,
        }
        return render(request, template, context)

class PostLike(View):
    """
    Likes for posts
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        user = request.user
        profile = user.userprofile

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(profile)
        else:
            post.likes.add(profile)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
