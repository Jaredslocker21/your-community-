from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class CommunityPost(models.Model):
    """ Community Post Model """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    member = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="member_posts"
    )

    updated_on = models.DateTimeField(auto_now=True)
    blurb = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
    )

    class Meta:
        """
        Dedending order the member posts in created order,
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns a string showing the title.
        """
        return str(self.title)

    def number_of_likes(self):
        """
        Return total amount of likes on a recipe
        """
        return self.likes.count()
     
# this class was taken from I think therefore I blog


class Comment(models.Model):
    """Comment Model"""
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.TextField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)      

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"