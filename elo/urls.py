from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from elo.views import tournaments, home, teams, team, other, tournament, country, rankings, countries, article, articles

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

    #GET BIGGEST FALLER AND BIGGEST GAINER
    url(r'^rankings/highest/$', rankings.get_gains_losses),


#******************************************TEAMS URLS**************************************
    #LIST OF ALL TEAMS
    url(r'^teams/$', teams.get_team_list),

    #SEARCH TEAM BY NAME
    url(r'^teams/search$', teams.search_team_by_name),


#******************************************TEAM URLS**************************************
    # DETAILS OF A SPECIFIC TEAM
    url(r'^teams/(?P<pk>[0-9]+)/details/$', team.get_team_detail),

    # GET LIST OF LATEST GAMES FOR A GIVEN TEAM
    url(r'^teams/(?P<pk>[0-9]+)/matches/$', team.get_latest_matches),

    # GET INTERESTING INFOMRATION ON A SPECIFIC TEAM
    url(r'^teams/(?P<pk>[0-9]+)/information/$', team.get_team_information),

    # GET TEAM RIVALS TABLE
    url(r'^teams/(?P<pk>[0-9]+)/rivals/$', team.get_team_rivals),

#*****************************************TEAM RANKED MATCH HISTORY**************************
    # GET ALL RANKED MATCHES FOR A GIVEN TEAM (PAGNATION?)
    url(r'^teams/(?P<pk>[0-9]+)/rankedmatches/$', team.get_all_matches),

    # GET RANKED MATCHES FOR DIAGRAM
    url(r'^teams/(?P<pk>[0-9]+)/rankhistory/$', team.get_team_ranking_history),

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

    #GET LIST OF ALL TEAMS FILTERED BY TOURNAMENT -- NOT IMPLEMENTED
    url(r'^tournaments/(?P<pk>[0-9]+)/teams/$', tournament.get_team_list_by_tournament),

#********************************************ARTICLES*********************************************
    # GET ARTICLE
    url(r'^articles/(?P<pk>[0-9]+)/$', article.get_article),

    # GET MOST RECENT GAMES FOR A TOURNAMENT
    url(r'^articles/$', articles.get_articles),


#******************************************OTHER URLS**************************************
    #ADD EMAIL TO NEWSLETTER Q
    url(r'^newsletter/$', other.post_email),

    #GET FAQS
    url(r'^faq/$', other.get_faq),
]

urlpatterns = format_suffix_patterns(urlpatterns)
