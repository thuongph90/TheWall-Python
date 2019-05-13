from django.db import models
from apps.login_app.models import register

class Messages(models.Model):
    users=models.ForeignKey(register, related_name="posts")
    message=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class comments(models.Model):
    message_id=models.ForeignKey(Messages, related_name="post_id")
    comment=models.TextField()
    user_id=models.ForeignKey(register, related_name="user_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
