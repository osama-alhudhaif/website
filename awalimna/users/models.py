from django.db import models

# Create your models here.

'''
تصميم كل نماذج بيانات الحسابات و هن:
1-reader
2-author
3-admin_reader
4-admin_author
5-super_admin_reader
6-super_admin_author
7-educational_center
8-educational_center_teacher
9-educational_center_student
10-owner
'''

# user model
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
    pass