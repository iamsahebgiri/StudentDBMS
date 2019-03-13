from django.db import models

# Create your models here.
class Student(models.Model):

    roll = models.IntegerField()
    standard = models.CharField(max_length=3)
    school = models.CharField(max_length=120)
    admission_no = models.IntegerField()

    fullname = models.CharField(max_length=80)
    f_name = models.CharField(max_length=80)
    m_name = models.CharField(max_length=80)
    goal = models.CharField(max_length=60)
    address = models.TextField()
    birth_date = models.DateField()
    blood_group = models.CharField(max_length=10)

    contact = models.CharField(max_length=50)
    social_links = models.CharField(max_length=200)
    profile_pic_link = models.CharField(max_length=80)

    def __str__(self):
        return self.fullname
