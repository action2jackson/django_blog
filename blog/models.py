from django.db import models
from django.utils import timezone

# register your models in admin.py
# Create your models here.
# Change models file = change to the database (make migrations)
class Post(models.Model):
    # ForeignKey = only can be used in the existing database.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # self basically means "set" || EX: set a published date, set to save
        self.published_date = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    # create a String representation
    def __str__(self):
        # Shows the title as a string instead of the number of blog posts
        return self.title

class Comment(models.Model):
    # Cascade for this example if a post gets deleted so does its comments
    # Post.objects.get(pk=2).comments.all() == shows all the comments because of related_name
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # Approve is originally false
    approved = models.BooleanField(default=False)

    # Call this function to approve a comment and save the approve
    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

# You can know what post the comment is from and what comment the post is from
