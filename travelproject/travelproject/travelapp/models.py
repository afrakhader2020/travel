from django.db import models

# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name

class Team1(models.Model):
    Team_name = models.CharField(max_length=250)
    Team_img = models.ImageField(upload_to='pics')
    Team_desc = models.TextField()

    def __str__(self):
        return self.Team_name

# class Team(models.Model):
#     name_team = models.CharField(max_length=250)
#     img_team = models.ImageField(upload_to='pics')
#     desc_team = models.TextField()
#
#     def __str__(self):
#         return self.name_team
