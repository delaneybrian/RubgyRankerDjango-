from rest_framework import serializers
from elo.models import Team, Tournament, Match, Country, Stadium, NewsletterEmails, FAQ, Rivals

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
        fields = ('id', 'name', 'rating', 'country', 'stadium', 'active', 'image_url', 'logo_url', 'description', 'website', 'max_rating', 'max_position', 'max_date', 'min_rating', 'min_position', 'min_date', 'lastweek_rating', 'lastweek_position', 'thisweek_rating', 'thisweek_position', 'current_streak', 'max_streak', 'played_matches')


class TeamShortSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'logo_url', 'active', 'country', 'thisweek_position', 'thisweek_rating')

class TeamRankingSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Team
        fields = ('id', 'name', 'logo_url', 'active', 'country', 'lastweek_rating', 'lastweek_position', 'thisweek_rating', 'thisweek_position')


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

class TournamentSuperShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'logo_url')

class MatchSerializer(serializers.ModelSerializer):
    hometeam = TeamShortSerializer(read_only=True)
    awayteam = TeamShortSerializer(read_only=True)
    tournament = TournamentShortSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('hometeam', 'hometeam_score', 'awayteam', 'awayteam_score', 'match_date', 'tournament')


class MatchShortSerializer(serializers.ModelSerializer):
    hometeam = TeamShortSerializer(read_only=True)
    awayteam = TeamShortSerializer(read_only=True)
    tournament = TournamentSuperShortSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('hometeam', 'hometeam_score', 'awayteam', 'awayteam_score', 'match_date', 'tournament')

class MatchLargeSerializer(serializers.ModelSerializer):
    hometeam = TeamShortSerializer(read_only=True)
    awayteam = TeamShortSerializer(read_only=True)
    tournament = TournamentSuperShortSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ('hometeam', 'hometeam_score', 'awayteam', 'awayteam_score', 'match_date', 'tournament', 'hometeam_rating_before', 'awayteam_rating_before', 'hometeam_rating_after', 'awayteam_rating_after')


class MatchDiagramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Match
        fields = ('hometeam', 'awayteam', 'match_date', 'hometeam_rating_after', 'awayteam_rating_after')


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

