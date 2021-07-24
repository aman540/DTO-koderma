from  django.db import models 

class Contact(models.Model):
    name=models.CharField(max_length=50,null=True)
    phone= models.CharField(max_length=10,null=True)
    email= models.CharField(max_length=50,null=True)
    queries=models.CharField(max_length=300,null=True)

    def __str__(self):
	    return self.name

   

class Two(models.Model):
    owner=models.CharField(max_length=50,null=True)
    regno=models.CharField(max_length=50,null=True)
    chalantype=models.CharField(max_length=50,null=True)
    amt=models.IntegerField()
    city=models.CharField(max_length=10,null=True)
    state=models.CharField(max_length=10,null=True)
    zip=models.IntegerField()

    def __str__(self):
	    return self.regno

class Four(models.Model):
    owner=models.CharField(max_length=50,null=True)
    regno=models.CharField(max_length=50,null=True)
    chalantype=models.CharField(max_length=50,null=True)
    amt=models.IntegerField()
    city=models.CharField(max_length=10,null=True)
    state=models.CharField(max_length=10,null=True)
    zip=models.IntegerField()

    def __str__(self):
	    return self.regno

class Nongear(models.Model):
    owner=models.CharField(max_length=50,null=True)
    regno=models.CharField(max_length=50,null=True)
    chalantype=models.CharField(max_length=50,null=True)
    amt=models.IntegerField()
    city=models.CharField(max_length=10,null=True)
    state=models.CharField(max_length=10,null=True)
    zip=models.IntegerField()   

    def __str__(self):
	    return self.regno  


class Apply(models.Model):
    name=models.CharField(max_length=200,null=True)
    email= models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=10,null=True)
    vtype=models.CharField(max_length=5,null=True)
    gender=models.CharField(max_length=5,null=True)
    def __str__(self):
	    return self.name
        





   


  

    

