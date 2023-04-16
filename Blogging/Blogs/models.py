from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=50, default = "No Title")
    content = models.TextField( default = "No Content Entered !")

    def __str__(self):
        return self.title
        