from django.db import models


class terrain_items(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    hexcolor = models.CharField(max_length=50)
    size = models.IntegerField()
    spread = models.CharField(max_length=50)
    affect = models.CharField(max_length=50)
    size = models.IntegerField()
    affectText = models.CharField(max_length=250)

class terrain_details(models.Model):
   name = models.CharField(max_length=50,primary_key=True)
   land_type = models.CharField(max_length=50)
   description = models.CharField(max_length=250)
   creatures = models.CharField(max_length=250)
   terrain_textures = models.CharField(max_length=500)


class bestiary(models.Model):
    key = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100)
    health = models.IntegerField()
    healthMaxVariance = models.IntegerField()
    move = models.IntegerField()
    size = models.IntegerField()
    move_type = models.CharField(max_length=50)
    render_type = models.CharField(max_length=50)
    group_min = models.IntegerField()
    group_max = models.IntegerField()
    color = models.CharField(max_length=50)
    perception = models.IntegerField()
    attack_type = models.CharField(max_length=250)
    damage = models.IntegerField()


