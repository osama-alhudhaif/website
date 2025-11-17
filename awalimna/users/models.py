from django.db import models
from django.conf import settings

# Create your models here.
USER_ROLE = [
    'reader',
    'author',
    'admin_reader',
    'admin_author',
    'super_admin_reader',
    'super_admin_author',
    'educational_center',
    'educational_center_teacher',
    'educational_center_student',
    'owner',
]

# user model
# OOP for all data in users models
class user(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# reader model
class reader(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# author model
class author(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stories = models.ManyToManyField('Story') #List of stories

# admin_reader model
class admin_reader(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# admin_author model
class admin_author(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# super_admin_reader model
class super_admin_reader(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# super_admin_author model
class super_admin_author(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# educational_center model
class educational_center(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# educational_center_teacher model
class educational_center_teacher(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# educational_center_student model
class educational_center_student(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# owner model
class owner(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=25)
    address = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10)
    level = models.CharField(max_length=10)
    country = models.CharField(max_length=25)
    status = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ip_address = models.CharField(max_length=25)

    def __str__(self):
        return self.username