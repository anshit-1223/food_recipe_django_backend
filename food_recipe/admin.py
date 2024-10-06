from django.contrib import admin
from .models import *
# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display=('id','title','description','ingredients','instructions','imgurl')

admin.site.register(Recipe,RecipeAdmin)

class SignupAdmin(admin.ModelAdmin):
    list_display=('name','email','passwd')
admin.site.register(Signup,SignupAdmin)