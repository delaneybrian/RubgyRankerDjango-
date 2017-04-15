from rest_framework import serializers
from elo.models import Team, Tournament, Match, Country, Stadium, RatingTimestamp, NewsletterEmails, FAQ, Rivals, CurrentRankingTable

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name' , 'hemisphire', 'flag_url')


class StadiumSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Stadium
        fields = ('name', 'capacity', 'image_url', 'country')


class TeamSerializer(serializers.ModelSerializer):
    stadium = StadiumSerializer(read_only=True, many=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'rating', 'country', 'stadium', 'active', 'image_url', 'logo_url', 'description', 'website')


class TeamShortSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'logo_url', 'active', 'country')


class TournamentSerializer(serializers.ModelSerializer):
    teams = TeamShortSerializer(read_only=True, many=True)
    countries = CountrySerializer(read_only=True, many=True)

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'countries', 'description', 'image_url', 'logo_url', 'teams', 'website')


class TournamentShortSerializer(serializers.ModelSerializer):
    countries = CountrySerializer(read_only=True, many=True)

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'logo_url', 'countries')


class MatchSerializer(serializers.ModelSerializer):
    hometeam = TeamShortSerializer(read_only=True)
    awayteam = TeamShortSerializer(read_only=True)
    tournament = TournamentShortSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('hometeam', 'hometeam_score', 'awayteam', 'awayteam_score', 'match_date', 'tournament')


class RatingSerializer(serializers.ModelSerializer):
    team = TeamShortSerializer(read_only=True)

    class Meta:
        model = RatingTimestamp
        fields = ("team", "date", "dated_rating")


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsletterEmails
        fields = ('__all__')


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('question', 'answer')


class RivalsSerializer(serializers.ModelSerializer):
    team_a = TeamShortSerializer(read_only=True)
    team_b = TeamShortSerializer(read_only=True)

    class Meta:
        model = Rivals
        fields  = ('wins', 'losses', 'draws', 'team_a', 'team_b')


class RankingSerializer(serializers.ModelSerializer):
    team = TeamShortSerializer(read_only=True)

    class Meta:
        model = CurrentRankingTable
        fields = ('team', 'rating', 'date', 'position', 'change')