from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Book)
admin.site.register(Borrowed)

# Register your models here.
