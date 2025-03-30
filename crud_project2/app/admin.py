from django.contrib import admin
from app.models import StudentModel
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone']
    
    
admin.site.register(StudentModel,StudentAdmin)