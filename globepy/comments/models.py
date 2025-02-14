from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, auth

class Comment(models.Model):
    comment_text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    def __str__(self):
        return f"Comment by {self.created_by.username} on {self.created_date}"
    
    def is_reply(self):
        return self.parent_comment is not None
        