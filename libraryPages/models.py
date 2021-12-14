from datetime import date, datetime,timedelta
from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser,PermissionsMixin
from django.db.models.deletion import CASCADE
from django.db.models.fields import DateField
from django.utils.translation import ugettext_lazy as _
from .managers import ProfileManager
from django.utils import timezone

class Profile(AbstractBaseUser,PermissionsMixin):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True,unique=True) 
    # password = models.CharField(max_length=50)
    college = models.CharField(max_length=50,default="fcai")
    ID = models.CharField(max_length=50,default="30011")
    phone = models.CharField(max_length=15,default="012")
    USERNAME_FIELD = 'email'
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    REQUIRED_FIELDS = []
    objects = ProfileManager()

    def __str__(self):
        return self.email



class Book(models.Model):
    TYPE_CATEGORY = (
    ('Fiction', 'Fiction'),
    ('Sceince','Science' ),
    ('Drama', 'Drama'),
    ('Crime', 'Crime')
    )
    # books_categories=['Science', 'Fiction', 'Drama', 'Crime']
    ISBN = models.CharField(max_length=13)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='photos/%y/%m/%d')
    publication_year = models.CharField(max_length=4)
    author_name =models.CharField(max_length=100)
    type = models.CharField(max_length=50, choices=TYPE_CATEGORY)
    counter= models.IntegerField(default=1)
    def __str__(self):
        return f'{self.name} By {self.author_name}'

def afterWeek():
    return datetime.now() + timedelta(days=7)

class Borrowed(models.Model):
    Date = DateField(default=datetime.now)
    DateReturn = DateField(default=afterWeek)
    bookId = models.ForeignKey(Book,on_delete=models.CASCADE)
    userEmail = models.ForeignKey(Profile,on_delete=models.CASCADE)
    extended = models.BooleanField(default=False)
    class Meta:
        unique_together = (('bookId','userEmail'),)
    