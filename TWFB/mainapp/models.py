from django.db import models
from ckeditor.fields import RichTextField,CKEditorWidget
import datetime
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from ckeditor_uploader.fields import RichTextUploadingField

class Item(models.Model):
    #img = models.ImageField(upload_to='pic', default= None)
    realname = models.CharField(max_length=30, default="None")
    content = RichTextUploadingField()
    dt = models.DateTimeField('DatetimeCommit')

    class Meta:
        ordering = ['dt']

    def __str__(self):
        return str(self.dt)+"_"+str(self.realname)+":"+str(self.content)

class LastPostID(models.Model):
    postdt = models.DateTimeField('DatetimeCommit')
    postid = models.IntegerField()


