from  django.db import models
from django.db.models.base import ModelState 
import os
from twilio.rest import Client


#contact model
class Contact(models.Model):
    date = models.DateTimeField()
    name=models.CharField(max_length=50,null=True)
    phone= models.CharField(max_length=10,null=True)
    email= models.CharField(max_length=50,null=True)
    queries=models.CharField(max_length=300,null=True)

    def __str__(self):
	    return self.name

class Grievance(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=20,null=True)
    phone= models.IntegerField( null = False)
    email = models.EmailField(null=True)
    file=models.FileField(upload_to='',null= True)
    subject= models.CharField(max_length=100,null=True)
    matter= models.TextField(null= False)  

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        account_sid = 'AC8202c1e823356c199aa7596e2864cb00'
        auth_token = '503d1cde8b369e76a4590952b8f0bfff'
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     body= f"{self.name},{self.email},{self.subject},{self.matter}",
                     from_='+19852289110',
                     to='+917260053209',
                 )

        print(message.sid)
        return super().save(*args,**kwargs)    
          

#two wheeler challan model
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
# four wheeler challan model
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
#nongear challan model
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
#checknama challan entrys
class Checknama(models.Model):
    date= models.DateTimeField()
    name=models.CharField(max_length=40,null=True)
    regno= models.CharField(max_length=10,null=True)
    vt= models.CharField(max_length=50,null=True)
    chalanno=models.IntegerField()

    def __str__(self):
	    return self.name

class FileUpload(models.Model):
    date=models.DateTimeField()
    subject=models.CharField(max_length=20,null=True)
    notesfile=models.FileField(upload_to='')
    filetype=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.subject






        





   


  

    

