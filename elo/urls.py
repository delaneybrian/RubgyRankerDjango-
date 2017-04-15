from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from elo.views import tournaments, home, teams, team, other, tournament, country, rankings, countries

urlpatterns = [
#******************************************HOME URLS**************************************
    #GET LIST OF CURRENT RANKINGS
    url(r'^home/rankings/$', home.get_rankings_list),

    #GET DETAILS OF RANKINGS FOR HOMEPAGE
    url(r'^home/details/$', home.get_rankings_detail),

    #GET LIST OF RECENT MATCHES
    url(r'^home/matches/$', home.get_latest_matches),

    #GET FEATURED TEAM
    url(r'^home/featured/$', home.get_featured_team),


#*****************************************RANKING URLS************************************
    #GET ALL RANKED TEAMS
    url(r'^rankings/$', rankings.get_rankings_list),


#******************************************TEAMS URLS**************************************
    #LIST OF ALL TEAMS
    url(r'^teams/$', teams.get_team_list),


#******************************************TEAM URLS**************************************
    # DETAILS OF A SPECIFIC TEAM
    url(r'^teams/(?P<pk>[0-9]+)/details/$', team.get_team_detail),

    # GET TEAM CURRENT RANKING
    url(r'^teams/(?P<pk>[0-9]+)/currentranking/$', team.currentranking),

    # GET LIST OF LATEST HOMEGAMES FOR A GIVEN TEAM
    url(r'^teams/(?P<pk>[0-9]+)/matches/home/$', team.get_latest_home_matches),

    # GET LIST OF LATEST AWAYGAMES FOR A GIVEN TEAM
    url(r'^teams/(?P<pk>[0-9]+)/matches/away/$', team.get_latest_away_matches),

    # GET INTERESTING INFOMRATION ON A SPECIFIC TEAM
    url(r'^teams/(?P<pk>[0-9]+)/information/$', team.get_team_information),

    # GET TEAM RIVALS TABLE
    url(r'^teams/(?P<pk>[0-9]+)/rivals/$', team.get_team_rivals),

    # GET HIGHEST AND LOWEST EVER RANKINGS FOR A TEAM
    url(r'^teams/(?P<pk>[0-9]+)/history/$', team.get_history),

#******************************************COUNTRIES URLS ***********************************
    # GET LIST OF ALL COUNTRUES
    url(r'^country/$', countries.get_countries),


#******************************************COUNTRY URLS**************************************
    #GET COUNTRY INFORMATION
    url(r'^country/(?P<pk>[0-9]+)/$', country.get_country_basic),

    #GET LIST OF ALL TEAMS FOR A COUNTRY
    url(r'^country/(?P<pk>[0-9]+)/teams/$', country.get_team_list_by_country),

    #GET LIST OF ALL tournaments FOR A COUNTRY
    url(r'^country/(?P<pk>[0-9]+)/tournaments/$', country.get_tournament_list_by_country),

    #GET INFORMATION ON A SPECIFIC COUNTRY
    url(r'^country/(?P<pk>[0-9]+)/information/$', country.get_country_information),


#******************************************TOURNAMENTS URLS**************************************
    # GET LIST OF ALL TOURNAMENTS
    url(r'^tournaments/$', tournaments.get_tournaments),


#******************************************TOURNAMENT URLS**************************************
    #GET DETAILS ON A SPECIFIC TOURNAMENT
    url(r'^tournaments/(?P<pk>[0-9]+)/$', tournament.get_tournament_details),

    #GET MOST RECENT GAMES FOR A TOURNAMENT
    url(r'^tournaments/(?P<pk>[0-9]+)/matches/$', tournament.get_touramanet_matches),

    #GET LIST OF ALL TEAMS FILTERED BY TOURNAMENT
    url(r'^tournaments/(?P<pk>[0-9]+)/teams/$', tournament.get_team_list_by_tournament),

#******************************************OTHER URLS**************************************
    #ADD EMAIL TO NEWSLETTER Q
    url(r'^newsletter/$', other.post_email),

    #GET FAQS
    url(r'^faq/$', other.get_faq),
]

urlpatterns = format_suffix_patterns(urlpatterns)
