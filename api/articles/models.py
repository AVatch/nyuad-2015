from django.db import models


class Article(models.Model):
    url = models.URLField(unique=True)
    domain = models.CharField(max_length=240, blank=True)

    title = models.CharField(max_length=240, blank=True)
    excerpt = models.TextField(blank=True)
    image = models.URLField(blank=True)

    bumpCount = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-bumpCount',)

    def __unicode__(self):
        return self.url
