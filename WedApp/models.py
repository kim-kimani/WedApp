from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class WeddingDetails(models.Model):
    bride = models.CharField(max_length=100)
    groom = models.CharField(max_length=100)
    day = models.CharField(max_length=100)
    date = models.DateField()
    bride_phone_number = models.CharField(max_length=100)
    groom_phone_number = models.CharField(max_length=100)
    ceremony_time = models.TimeField()
    ceremony_venue = models.CharField(max_length=100)
    ceremony_location = models.CharField(max_length=100)
    reception_name = models.CharField(max_length=100)
    reception_location = models.CharField(max_length=100)
    reception_time = models.TimeField()
    
    def __str__(self):
        return self.bride
    
class Media(models.Model):
    image = models.ImageField(upload_to='media', blank=True, null=True)
    video = models.FileField(upload_to='media', blank=True, null=True)
    logo = models.FileField(upload_to='media', blank=True, null=True)
    bride_n_groom = models.ImageField(upload_to='media', blank=True, null=True)
    bride = models.ImageField(upload_to='media', blank=True, null=True)
    groom = models.ImageField(upload_to='media', blank=True, null=True)
    
    
class RSVP(models.Model):
    ATTENDANCE = [
        ('yes', 'Yes, I will attend'),
        ('no', 'No, I will not attend'),
    ]
    message = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    attendance = models.CharField(max_length=100, choices=ATTENDANCE)
    guest_count = models.PositiveBigIntegerField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Message(models.Model):
    RECIPIENT_CHOICES = [
        ('bride', 'Bride'),
        ('groom', 'Groom'),
        ('both', 'Both')
    ]

    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    recipient = models.CharField(max_length=10, choices=RECIPIENT_CHOICES, default='both')
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.get_recipient_display()}"
    
class Gallery(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="media/gallery")
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.uploaded_on}"
