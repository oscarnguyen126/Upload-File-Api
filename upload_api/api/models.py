from django.db import models


class UploadedFile(models.Model):
    file = models.FileField()  # file location
    uploaded_on = models.DateTimeField(auto_now_add=True)
    target_class = models.CharField(max_length=100, null=True, blank=True)
    target_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.uploaded_on.date()
