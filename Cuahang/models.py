from django.db import models

# Create your models here.
class Chungloai(models.Model):
    Chungloai_id=models.CharField(max_length=150,primary_key=True)
    Anh=models.FileField(null=True)
    def __str__(self):
        return self.Chungloai_id
class Linhkien(models.Model):
    Chungloais = models.ForeignKey(Chungloai, on_delete=models.CASCADE, null=True)
    Linhkien_id=models.CharField(max_length=150,primary_key=True)
    Anh=models.FileField(null=True)
    Chitiet=models.TextField()
    Gia=models.FloatField(  )
    Thoigian = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Linhkien_id

