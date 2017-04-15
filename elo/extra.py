import datetime

def convert_date(match_dict):
    match_date = match_dict["match_date"].split(' ')
    match_date = match_date[0].split('-')
    match_date = datetime.datetime(int(match_date[0]), int(match_date[1]), int(match_date[2]))
    return match_date