from django.db import models
from cloudinary.models import CloudinaryField

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    link = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name="projects")
    image = CloudinaryField(
        'image',
        folder='projects'
    )

    def __str__(self):
        return self.name
    
class ContactDetails(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name} - {self.subject}"

# Note: 
# ForeignKey - we use when we wants to perform operation with single data.
# We use ManyToManyField - to deal with multiple data.
