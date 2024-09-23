# profiles/models.py
from django.db import models
from menu.models import Food
from django.utils.translation import gettext_lazy as _

class Comment(models.Model):
    food = models.ForeignKey(Food, on_delete = models.CASCADE , related_name = 'comments')
    name = models.CharField(max_length = 35)
    email = models.EmailField(null = True , blank = True)
    body = models.TextField(_('نظر'), blank = False, null = False)
    date_added = models.DateTimeField(_('تاریخ اضافه شدن'), auto_now_add = True)
    active = models.BooleanField(default = False)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
