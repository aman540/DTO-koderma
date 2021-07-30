from  django.db import models
from django.db.models.base import ModelState 


class Contact(models.Model):
    date = models.DateTimeField()
    name=models.CharField(max_length=50,null=True)
    phone= models.CharField(max_length=10,null=True)
    email= models.CharField(max_length=50,null=True)
    queries=models.CharField(max_length=300,null=True)

    def __str__(self):
	    return self.name

        

   

class Two(models.Model):
    date = models.DateTimeField()
    owner=models.CharField(max_length=50,null=True)
    regno=models.CharField(max_length=50,null=True)
    chalantype=models.CharField(max_length=50,null=True)
    amt=models.IntegerField()

    class Meta:
        db_table="dto_two"
   

    def __str__(self):
	    return self.regno

class Four(models.Model):
    date = models.DateTimeField()
    owner=models.CharField(max_length=50,null=True)
    regno=models.CharField(max_length=50,null=True)
    chalantype=models.CharField(max_length=50,null=True)
    amt=models.IntegerField()

    class Meta:
        db_table="dto_four"
   

    def __str__(self):
	    return self.regno

class Nongear(models.Model):
    date = models.DateTimeField()
    owner=models.CharField(max_length=50,null=True,)
    regno=models.CharField(max_length=50,null=True)
    chalantype=models.CharField(max_length=50,null=True)
    amt=models.IntegerField()
   
    class Meta:
        db_table="dto_nongear" 

    def __str__(self):
	    return self.regno  



        





   


  

    

