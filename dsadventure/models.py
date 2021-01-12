from django.db import models


class terrain_items(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    hexcolor = models.CharField(max_length=50, default="#000000")
    borderhex = models.CharField(max_length=50, default="#000000")
    size = models.IntegerField()
    spread = models.CharField(max_length=50)
    spread_radius = models.IntegerField()
    affect = models.CharField(max_length=50)
    size = models.IntegerField()
    affectText = models.CharField(max_length=250)
    abundance_affected_by = models.CharField(max_length=50)
    density_affected_by = models.CharField(max_length=50)
    render_index = models.IntegerField(default="-1")


class terrain_details(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    land_type = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    creatures = models.CharField(max_length=250)
    terrain_textures = models.CharField(max_length=500)


class bestiary(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
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
    xp = models.IntegerField()


class buildings(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    shape = models.CharField(max_length=50, default="rect")
    door = models.CharField(max_length=50, default="open")
    guards = models.CharField(max_length=50, default="none")
    messages = models.CharField(max_length=250, default="welcome **name**")


class events(models.Model):
    key = models.CharField(max_length=100, primary_key=True)
    agent_type = models.CharField(max_length=100, default="nation")
    n_subjects = models.IntegerField()
    n_objects = models.IntegerField()
    event = models.CharField(max_length=250)
    effect_var = models.CharField(max_length=50, default="favor")
    effect = models.DecimalField(max_digits=10, decimal_places=2)
    a_message = models.CharField(max_length=250)
    o_message = models.CharField(max_length=250)

