from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Qna(models.Model):
    title = models.CharField(max_length = 200)
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    body = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class QnaComment(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    qna = models.ForeignKey(Qna, null=False, blank=False, on_delete=models.CASCADE)
    comment_like = models.ManyToManyField(User, related_name='comment_likes', blank=True)
    comment_like_count = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.qna.title+ " : " + self.content
    
class QnaReply(models.Model):
    content = models.TextField()
    pub_date = models.DateTimeField()
    writer = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    comment = models.ForeignKey(QnaComment, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment.qna.title + " - Comment: " + self.comment.content + " - Reply: " + self.content