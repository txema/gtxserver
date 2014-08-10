from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from simple_history.models import HistoricalRecords

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())

# Create your models here.


class Status(models.Model):
    status = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.status

    class Meta:
        #app_label = 'statuses'
        db_table = 'status'


class Tag(models.Model):
    tag = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.tag

    class Meta:
        #app_label = '
        db_table = 'tag'

class Task(models.Model):
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    owner = models.ForeignKey('auth.User', related_name='tasks_assigned')
    created_by = models.ForeignKey('auth.User', related_name='tasks_created')
    statuses = models.ManyToManyField(Status, null=False)
    tags = models.ManyToManyField(Tag, null=True)
    history = HistoricalRecords()


    def __unicode__(self):
        return self.description

    class Meta:
        db_table = 'tasks'
        ordering = ['created_at']



