from django.db import models
from django.core.validators import MinValueValidator
from Person.models import * 
import datetime

# Create your models here.



def dateValidator(value):
    if not value >= datetime.date.today():
        raise ValidationError(
            "Date must be in the future"
        )

class Event (models.Model):
    
    def __str__(self):
        return self.title
    
    CATEGORY_CHOICES = (
        ('Music', 'Music'),
        ('Cinema', 'Cinema'),
        ('Sport', 'Sport'),
    )
    
    title = models.CharField(max_length=255, null=True)
    description=models.TextField(("description"))
    evt_date=models.DateField(validators=[dateValidator])
    image = models.ImageField(upload_to='images/', blank=True)
    state = models.BooleanField(default=False)
    nbe_participant= models.IntegerField(default=0 , validators= [MinValueValidator(0,message="This value should be greater than or equal to zero")])
    Category=models.CharField(choices=CATEGORY_CHOICES,max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
   
    #association
    organizer = models.ForeignKey(Person , on_delete=models.PROTECT )
    
    #participants=models.ManyToManyField(Person)
    
    
    