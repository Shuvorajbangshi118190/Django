from django.db import models

# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    messenger = models.CharField(max_length=100)
    sender = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE,related_name='blog_posts')
    title = models.CharField(max_length=100)
    details= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    def __str__(self):
     return self.title