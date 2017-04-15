from django.contrib import admin
from elo.models import Match, Team, Stadium, Country, Tournament, RatingTimestamp, NewsletterEmails, FAQ

class TeamAdmin(admin.ModelAdmin):
    model = Team
    readonly_fields = ('id',)
    ordering = ('-rating',)

class TournamentAdmin(admin.ModelAdmin):
    model = Tournament
    readonly_fields = ('id',)

class MatchAdmin(admin.ModelAdmin):
    model = Match
    readonly_fields = ('id',)

# Register your models here.
admin.site.register(Team, TeamAdmin)
admin.site.register(Match, MatchAdmin)
admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Stadium)
admin.site.register(Country)
admin.site.register(RatingTimestamp)
admin.site.register(NewsletterEmails)
admin.site.register(FAQ)