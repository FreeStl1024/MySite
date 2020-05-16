from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class BaseModel(models.Model):
    #The base Model of App post 
    class Meta:
        abstract = True
        ordering = ['-created_time']
    created_time = models.DateTimeField(auto_now_add=True,help_text=u'created time')
    last_modified = models.DateTimeField(auto_now=True, help_text=u'changed time')
    def __str__(self):
        raise NotImplementedError

class Topic(BaseModel):
    #the topic accaimed in BBS Forum
    title = models.CharField(max_length=255, unique=True, help_text='Title')
    content = models.TextField(help_text=u'Contains')
    is_online = models.BooleanField(default=True, help_text=u'Is/not the topic online')
    user = models.ForeignKey(to=User, to_field='id', on_delete=models.CASCADE, help_text=u'Associated user table')
    def __str__(self):
        return '%d: %s' % (self.id, self.title[0:20])

class Comment(BaseModel):
    #the talks about the topic of BBS Forum
    content = models.CharField(max_length=255, help_text='The talks')
    topic = models.ForeignKey(to=Topic, to_field='id', on_delete=models.CASCADE, help_text=u'Associated topic table')
    up = models.IntegerField(default=0, help_text=u'support')
    down = models.IntegerField(default=0, help_text=u'against')
    def __str__(self):
        return '%d: %s' % (self.id, self.content[0:20])