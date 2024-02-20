from django.db import models

# Create your models here.
class state(models.Model):
    state=models.CharField(max_length=90)
    def __str__(self):
        return self.state

class district(models.Model):
    district=models.CharField(max_length=90)
    state=models.ForeignKey(state, on_delete=models.CASCADE)
    def __str__(self):
        return self.district

class qualification(models.Model):
    qualification=models.CharField(max_length=90)
    def __str__(self):
        return self.qualification

class enquirysource(models.Model):
    enquirysource=models.CharField(max_length=90)
    def __str__(self):
        return self.enquirysource
followupchoices=(
        ('yes','YES'),
        ('no','NO'),
    )
class followupstatus(models.Model):
    followupstatus=models.CharField(max_length=90, choices=followupchoices)
    def __str__(self):
        return self.followupchoices

class syllabus(models.Model):
    syllabus=models.CharField(max_length=90)
    def __str__(self):
        return self.syllabus

class course(models.Model):
    course=models.CharField(max_length=90)
    def __str__(self):
        return self.course

class branch(models.Model):
    phonenumber=models.IntegerField()
    company=models.CharField(max_length=90)
    address1=models.TextField()
    address2=models.TextField()
    address3=models.TextField()
    email=models.EmailField()
    def __str__(self):
        return self.company

class student(models.Model):
    name=models.CharField(max_length=90)
    company=models.CharField(max_length=90)
    state=models.CharField(max_length=90)
    district=models.CharField(max_length=90)
    qualification=models.CharField(max_length=90)
    course=models.CharField(max_length=90)
    def __str__(self):
        return self.name
    
    
    

  
    
    

    

    
    