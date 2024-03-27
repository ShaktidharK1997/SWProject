from django.db import models

from django.conf import settings

class Author(models.Model):
    authorID = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=150)
    email = models.EmailField(null=True)

class Paper(models.Model):
    paperID = models.CharField(primary_key=True, max_length=50)
    year = models.IntegerField(null=True)
    title = models.CharField(max_length=512)
    abstract = models.TextField()
    authors = models.ManyToManyField(Author, through='PaperAuthors', related_name='papers')

class PaperAuthors(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, to_field='authorID')
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, to_field='paperID')

class PersonalInfo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    location = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    contact = models.CharField(max_length=15)
    # Additional fields as needed

class Education(models.Model):
    personal_info = models.ForeignKey(PersonalInfo, related_name='education', on_delete=models.CASCADE)
    university = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    # Additional fields as needed