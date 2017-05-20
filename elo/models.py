from django.db import models
from django.utils import timezone




class Country(models.Model):
    NORTHERN = "NORTHERN"
    SOUTHERN = "SOUTHERN"
    HEMISPHIRE_CHOICES = (
        (NORTHERN, 'Northern'),
        (SOUTHERN, 'Southern'))

    name = models.CharField(max_length=100)
    hemisphire = models.CharField(choices=HEMISPHIRE_CHOICES, default="Northern", max_length=10)
    flag_url = models.CharField(max_length=400)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=200)
    capacity = models.IntegerField(null=True, blank=True)
    image_url = models.CharField(max_length=400)
    country = models.ForeignKey(Country)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=1500)
    created_date = models.DateTimeField(default=timezone.now)
    country = models.ForeignKey(Country)
    stadium = models.ManyToManyField(Stadium)
    active = models.BooleanField(default=True)
    image_url = models.CharField(max_length=400)
    logo_url = models.CharField(max_length=400)
    description = models.TextField()
    website = models.CharField(max_length=400, default="Unknown")
    max_rating = models.IntegerField(default=0)
    max_position = models.IntegerField(default=4000)
    max_date = models.DateTimeField(null=True, blank=True)
    min_rating = models.IntegerField(default=4000)
    min_position = models.IntegerField(default=0)
    min_date = models.DateTimeField(null=True, blank=True)
    lastweek_rating = models.IntegerField(default=1500)
    thisweek_rating = models.IntegerField(default=1500)
    lastweek_position = models.IntegerField(default=0)
    thisweek_position = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    max_streak = models.IntegerField(default=0)
    played_matches = models.IntegerField(default=0)


    def __str__(self):
        return self.name + " - " + str(self.rating)

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    teams = models.ManyToManyField(Team, null=True, blank=True, related_name="tournaments")
    countries = models.ManyToManyField(Country)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=400)
    logo_url = models.CharField(max_length=400)
    website = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Match(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=300)
    hometeam = models.ForeignKey(Team, related_name="home_matches")
    hometeam_score = models.IntegerField()
    awayteam = models.ForeignKey(Team, related_name="away_matches")
    awayteam_score = models.IntegerField()
    match_date = models.DateTimeField()
    tournament = models.ForeignKey(Tournament, null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    calculated = models.BooleanField(default=False)
    hometeam_rating_after = models.IntegerField(default=0)
    awayteam_rating_after = models.IntegerField(default=0)
    hometeam_rating_before = models.IntegerField(default=0)
    awayteam_rating_before = models.IntegerField(default=0)

    def __str__(self):
        return  str(self.hometeam_score) + " v " + " " + str(self.awayteam_score) + " - " + str(self.match_date.date())

class Rivals(models.Model):
    team_a = models.ForeignKey(Team, related_name="rival_A")
    team_b = models.ForeignKey(Team, related_name="rival_B")
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)

    def __str__(self):
        return str(str(self.team_a) + " - " + str(self.team_b))

class NewsletterEmails(models.Model):
    email_address = models.EmailField(primary_key=True)

    def __str__(self):
        return str(self.email_address)

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    importance = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.question)

class Article(models.Model):
    mainheading = models.CharField(max_length=1000)
    mainimage = models.FileField(null=True, blank=True)
    subimage = models.FileField(null=True, blank=True)
    subheading = models.CharField(max_length=1000, null=True, blank=True)
    htmlcontent = models.TextField()
    author = models.CharField(max_length=100)
    footer = models.TextField(null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.mainheading)