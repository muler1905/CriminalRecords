from email.policy import default
from random import choices
from django.db import models

# Create your models here.
 

# reg_choice=(("Amhara Region Prison Police","Amhara Region Prison Police"))

class CentralPrison(models.Model):
    Name=models.CharField(max_length=100,default="Amhara Region Prison Police") 
    
    def __str__(self):
        return self.Name
        
 
class Prison(models.Model): 
    PrisonName=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Region = models.ForeignKey(CentralPrison,null=True,   on_delete=models.CASCADE)

    # Region=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.PrisonName