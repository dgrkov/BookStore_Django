from django.db import models
import datetime

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    dob = models.DateField()
    @property
    def age(self):
        # return (datetime.datetime.now().year - self.dob.year)
        if(self.dod):
           today = self.dod
        else:
            today = datetime.datetime.today()
        years_diff = today.year - self.dob.year
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            years_diff -= 1
        return years_diff
    dod = models.DateField(null=True, blank=True);
    def __str__(self):
        return self.first_name + " " + self.last_name

class Book(models.Model):
    COVER_TYPE = [
        ("H", "Hardcover"),
        ("P", "Paperback"),
        ("E", "E-book"),
    ]
    GENRE = [
        ("R", "Romance"),
        ("D", "Drama"),
        ("T", "Thriller"),
        ("F", "Fantasy"),
        ("S", "Sci-Fi"),
        ("H", "Horror"),
        ("M", "Mystery"),       
    ]
    title = models.CharField(max_length=100)
    num_pages = models.IntegerField()
    cover = models.CharField(max_length=1, choices=COVER_TYPE)
    genre = models.CharField(max_length=1, choices=GENRE)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    cover_picture = models.ImageField(upload_to='covers/')
    published = models.DateField()
    available_copies = models.IntegerField()
    sold_out = models.BooleanField(default=False)
    price = models.FloatField();

    def __str__(self):
        return self.title
    
