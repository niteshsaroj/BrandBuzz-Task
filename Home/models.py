from django.db import models

class ContactModel(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject = models.CharField(max_length=200)
    message= models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
