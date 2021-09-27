from django.contrib import admin
from dto.models import Contact,Two,Four,Nongear,Checknama,FileUpload,Grievance

class GrievanceAdmin(admin.ModelAdmin): 
    list_display= ['name','phone','email','file','subject','matter']
# Register your models here.
admin.site.register(Contact)
admin.site.register(Two)
admin.site.register(Four)
admin.site.register(Nongear)
admin.site.register(Checknama)
admin.site.register(FileUpload)
admin.site.register(Grievance ,GrievanceAdmin)

