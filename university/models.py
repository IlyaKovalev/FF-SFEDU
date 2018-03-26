from django.db import models

class Lecturer(models.Model):
    Name = models.CharField(max_length=70)
    degree = models.CharField(max_length=100)
    cathedra = models.CharField(max_length=100)
    additional_info = models.CharField(max_length=10000)
    seniority = models.IntegerField(default=0)
    image = models.CharField(max_length=500)
    work = models.CharField(max_length=100,default='доцент')
    def __str__(self):
        return self.Name
class Disciplines(models.Model):
    lecturer_id = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    discipline = models.CharField(max_length=500)
    def __str__(self):
        return self.discipline
class Publications(models.Model):
    lecturer_id = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    publication = models.CharField(max_length=900)
