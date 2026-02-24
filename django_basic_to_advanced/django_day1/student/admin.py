from django.contrib import admin
from student.models import Profile, Result
# Register your models here.




class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','roll','city')

admin.site.register(Profile,ProfileAdmin)


# admin.site.register(Result)

@admin.register(Result)
class ResuktAdmin(admin.ModelAdmin):
    list_display = ('id', 'stu_class')


