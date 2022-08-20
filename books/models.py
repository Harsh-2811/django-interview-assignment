from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=20)
    status = models.CharField(choices=[('BORROWED','BORROWED'),('AVAILABLE','AVAILABLE')],max_length=20,default="AVAILABLE")
    added_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    borrowd_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True,related_name="borrower")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class History(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrowd_by = models.ForeignKey(User,on_delete=models.CASCADE)
    borrow_date = models.DateField(null=True,blank=True)
    returned_date = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)