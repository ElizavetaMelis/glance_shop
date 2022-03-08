from django.db import models


class Catalog(models.Model):

    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Catalog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
