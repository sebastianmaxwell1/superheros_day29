from django.db import models


# Create your models here.
# superhero’s name, alter ego, primary superhero ability, secondary superhero ability, and catchphrase.
class Superhero(models.Model):
    # superheros = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    ability = models.CharField(max_length=50)
    secondary_superhero_ability = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name
