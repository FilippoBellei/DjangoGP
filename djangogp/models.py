from django.db.models import *


class Rider(Model):
    name = CharField(max_length=255)
    country = CharField(max_length=255)
    team = CharField(max_length=255)
    bike = CharField(max_length=255)
    dateOfBirth = DateField()
    placeOfBirth = CharField(max_length=255)
    height = IntegerField()
    weight = IntegerField()

    def __str__(self):
        return self.name


class Race(Model):
    name = CharField(max_length=255)
    city = CharField(max_length=255)
    date = DateField()
    temperature = IntegerField()
    weather = CharField(max_length=255)
    trackCondition = CharField(max_length=255)
    humidity = IntegerField()
    groundTemperature = IntegerField()

    def __str__(self):
        return self.name


class Result(Model):
    position = IntegerField()
    points = IntegerField(editable=False)
    rider = ForeignKey(Rider, on_delete=PROTECT)
    race = ForeignKey(Race, on_delete=PROTECT)

    def __str__(self):
        return f"{self.race} {self.position}"

    def save(self):
        match self.position:
            case 1:
                self.points = 25
            case 2:
                self.points = 20
            case 3:
                self.points = 16
            case 4:
                self.points = 13
            case 5:
                self.points = 11
            case 6:
                self.points = 10
            case 7:
                self.points = 9
            case 8:
                self.points = 8
            case 9:
                self.points = 7
            case 10:
                self.points = 6
            case 11:
                self.points = 5
            case 12:
                self.points = 4
            case 13:
                self.points = 3
            case 14:
                self.points = 2
            case 15:
                self.points = 1
            case _:
                self.points = 0
        super(Result, self).save()


class Standings(Model):
    position = IntegerField()
    points = IntegerField()
    rider = ForeignKey(Rider, on_delete=PROTECT)

    def __str__(self):
        return str(self.position)

    class Meta:
        verbose_name_plural = "Standings"
