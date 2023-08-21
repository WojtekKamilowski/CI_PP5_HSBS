from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.utils.text import slugify
import datetime


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    Model for blog post
    """
    post_title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                               related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    post_image = models.ImageField(blank=True)
    blog_excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(choices=STATUS, default=0)
    likes = models.ManyToManyField(UserProfile,
                                   related_name='blogpost_like',
                                   blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.post_title

    def save(self, *args, **kwargs):
        strtime = "".join(str(datetime.datetime.now()).split("."))
        string = "%s-%s" % (strtime[7:], self.post_title)
        self.slug = slugify(string)
        super(Post, self).save(*args, **kwargs)

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Model for user's comment
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    username = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.username.username}"
