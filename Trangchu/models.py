from django.db import models

# Create your models here.
class Linhvuc(models.Model):
    Linhvuc_id=models.CharField(max_length=150,primary_key=True)
    Anh=models.FileField(null=True)
    def __str__(self):
        return self.Linhvuc_id
class Sanpham(models.Model):
    Linhvucs=models.ForeignKey(Linhvuc,on_delete=models.CASCADE,null=True)
    Sanpham_id=models.CharField(max_length=150,primary_key=True)
    Anh=models.FileField(null=True,help_text='Anh cho linh kien')
    Mieuta=models.TextField()
    Filekem=models.FileField(null=True,blank=True)
    Caukien=models.TextField(null=True)
    Date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return  self.Sanpham_id
class Cacsanpham(Sanpham):
    pass


