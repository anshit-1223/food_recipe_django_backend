from django.db import models

# Create your models here.
class Recipe(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    ingredients=models.TextField()
    instructions=models.TextField()
    imgurl=models.URLField(default='https://static-00.iconduck.com/assets.00/404-page-not-found-illustration-512x496-zifaajyp.png');

    def __str__(self):
        return self.title
    
class Signup(models.Model):
    name=models.TextField(max_length=100)
    email=models.EmailField(primary_key=True)
    passwd=models.CharField()

    def __str__(self):
        return self.name