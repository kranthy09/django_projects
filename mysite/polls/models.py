from django.db import models

# Create your models here.

class Question(models.Model):
    text = models.TextField()
    name = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname  = models.CharField(max_length=50)
    def __str__(self):
        return self.name

# class Person(models.Model):
#     """
#     Each field is specified as model class attribute and each attribute maps
#     to database column
#     """
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)

class Manufacturer(models.Model):
    pass

class Car(models.Model):
    company_that_makes_it = models.ForeignKey(Manufacturer, 
                                    on_delete=models.CASCADE)

class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Person(models.Model):
    name = models.CharField(max_length=120, default="")


class Group(models.Model):
    name = models.CharField(max_length=120)
    members = models.ManyToManyField(Person, through="Membership")
    

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)