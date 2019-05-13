from django.db import models
class BlogManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="first_name should be at least 2 chars."
        if len(postData['last_name'])<2:
            errors['last_name']="last_name should be at least 2 chars."
        if len(postData['email'])<5:
            errors['email']="email is invalid"
        if len(postData['password'])<8:
            errors['first_name']="password should be at least 8 chars."
        if postData['password']!=postData['repassword']:
            errors['first_name']="password should match"
        return errors
    def account_validator(self,postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="first_name should be at least 2 chars."
        if len(postData['last_name'])<2:
            errors['last_name']="last_name should be at least 2 chars."
        if len(postData['email'])<5:
            errors['email']="email is invalid"
        return errors

class register(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=250)
    password=models.CharField(max_length=25)
    objects=BlogManager()
