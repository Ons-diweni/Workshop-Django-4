from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator,RegexValidator

# Create your models here.

#Validators
def emailValidator (value):
    if str(value).endswith('@esprit.tn') == False:
      raise ValidationError("mail inapproprié")


# un modèle utilisateur personnalisé qui étend de la classe AbstractUser (l'utilisateur par dèfaut de Django qui contien dèja quelques champs prédéfinis )
class Person(AbstractUser) :
    
  def __str__(self):
        return self.username
  
  password = models.CharField(max_length=7)  
  username = models.CharField("Username", max_length=255, unique=True)  
  cin = models.CharField(("cin"), max_length=8 , primary_key=True , validators=[RegexValidator(regex='^[0-9]{8}$',message="Cin must contain only 8 numbers")])
  email=models.EmailField(validators=[emailValidator])
  #email=models.EmailField(validators=[EmailValidator(whitelist=["esprit.tn"])])

  USERNAME_FIELD = 'username'


