from django.db import models


class Grape(models.Model):
    #aka Varietal
    common_name = models.CharField(max_length=50)
    latin_name = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.common_name


class Country(models.Model):
    iso_code = models.CharField(max_length=2, unique=True)
    name_english = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name_english


    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'


class Appellation(models.Model):
    appellation_name = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    def __unicode__(self):
        return self.appellation_name


class Winemaker(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Wine(models.Model):
    name = models.CharField(max_length=255)
    producer = models.ForeignKey(Winemaker)
    appellation = models.ForeignKey(Appellation)
    grapes = models.ManyToManyField(Grape)
    # year = models.SmallIntegerField(verbose_name='Vintage')


    def __unicode__(self):
        return self.name


#Grapes plural, mixture, with proportions
#Region - what area in a country? (geo info for showing on a map)
#Style - Fruity, Earthy?
#Type = Red, White, Rose,
#Bubbly?
#Alcohol content