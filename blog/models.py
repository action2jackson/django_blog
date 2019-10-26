from django.db import models
from django.utils import timezone

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

    # create a String representation
    def __str__(self):
        # Shows the title as a string instead of the number of blog posts
        return self.title
