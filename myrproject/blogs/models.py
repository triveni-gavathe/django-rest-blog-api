from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_title=models.CharField(max_length=100)
    blog_body=models.TextField()
    
    def __str__(self):
        return self.blog_title
    
class Comment(models.Model):
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    Comment=models.TextField()
    
    def __str__(self):
        return self.Comment
        
class Profile(models.Model):
    ROLE_CHOICES=(
        ('author','Author'),
        ('reader','Reader')
        
    ) 
    user=models.OneToOneField(User, on_delete=models.CASCADE)   
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default='render')
    def __str__(self):
        return f"{self.role}, {self.user}"