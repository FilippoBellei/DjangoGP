from django.db import models


class Rider(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    team = models.CharField(max_length=255)
    bike = models.CharField(max_length=255)
    dateOfBirth = models.DateField()
    placeOfBirth = models.DateField()
    height = models.IntegerField()
    peso = models.IntegerField()


class Race(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    date = models.DateField()
    temperature = models.IntegerField()
    wheather = models.CharField(max_length=255)
    trackCondition = models.CharField(max_length=255)
    humidity = models.IntegerField()
    groundTemperature = models.IntegerField()


class Result(models.Model):
    position = models.IntegerField()
    points = models.IntegerField()
    rider = models.ForeignKey(Rider, on_delete=models.PROTECT)
    race = models.ForeignKey(Race, on_delete=models.PROTECT)


class Standings(models.Model):
    position = models.IntegerField()
    points = models.IntegerField()
    rider = models.ForeignKey(Rider, on_delete=models.PROTECT)
