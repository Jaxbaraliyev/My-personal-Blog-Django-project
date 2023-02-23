from django.db import models

class Maqolalar(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField(auto_now_add=True)
    rasm = models.FileField(upload_to='images')
    matn = models.TextField()

    def __str__(self):
        return self.sarlavha

class Intervyu(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField(auto_now_add=True)
    link = models.CharField(max_length=100)

    def __str__(self):
        return self.sarlavha

class Comment(models.Model):
    matn = models.CharField(max_length=200)
    ism = models.CharField(max_length=30)
    sana = models.DateField(auto_now_add=True)
    maqola = models.ForeignKey(Maqolalar, on_delete=models.CASCADE)