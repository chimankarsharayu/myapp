from django.db import models

# Create your models here.
class homeTable(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=100,null=True, blank=True)
    image=models.ImageField(upload_to='images/', null=True, blank=True)
    value=models.IntegerField()
    
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    class Meta: 
         db_table ='homeTable'

    def __str__(self):
        return self.name
     