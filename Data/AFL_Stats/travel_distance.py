def team_travel(team, next_venue):
    # Measures distance travelled between games
    # Assumed all teams will leave from home state
    if team == 'Geelong' and next_venue == 'Kardinia Park':
        return 0
    team_location = find_team_loaction(team)
    if team == 'Brisbane' and next_venue == 'Gabba':
        return 0
    if team == 'Gold Coast' and next_venue == 'Carrara':
        return 0
    venue_location = find_venue_location(next_venue)

    return get_distance(team_location, venue_location)

    # Geelong = 0 if next_venue is Kardinia Park else loc = MEL
    # Brisbane = 0 for Gabba else QLD
    # Gold Coast = 0 for Carrara else QLD

    # Geelong, Brisbane and Gold Coast are all unique with home grounds


def find_team_loaction(team):
    melbourneTeams = ['Carlton', 'Collingwood','Essendon','Hawthorn','Melbourne',
    'North Melbourne','Richmond','St Kilda','Western Bulldogs']
    sydneyTeams = ['Greater Western Sydney','Sydney']
    adelaideTeams = ['Adelaide','Port Adelaide']
    perthTeams = ['Fremantle','West Coast']
    if team in melbourneTeams:
        return "MEL"
    if team in sydneyTeams:
        return "SYD"
    if team in adelaideTeams:
        return "ADE"
    if team in perthTeams:
        return "PER"
    if team == 'Geelong':
        return 'GEE'
    else:
        return team


def find_venue_location(venue):
    VenueList = {
        "CH" : ['Jiangwan Stadium'],
        "MEL" : ['M.C.G.', 'Docklands'],
        "VIC" : ['Kardinia Park', 'Eureka Stadium'],
        "SYD" : ['Blacktown', 'S.C.G.', 'Stadium Australia', 'Sydney Showground'],
        "QLD" : ["Cazaly's Stadium",  'Riverway Stadium', 'Carrara', 'Gabba'],
        "NT" : ['Marrara Oval', 'Traeger Park' ],
        "SA" : ['Adelaide Oval', 'Football Park'],
        "WA" : ['Perth Stadium',  'Subiaco'],
        "ACT" : [ 'Manuka Oval' ],
        "TAS" : ['Bellerive Oval', 'Bellerive Oval'],
        "NZ" :  ['Wellington']
    }
    for key, value in VenueList.items():
        if venue in value:
            return key


def get_distance(team, next_venue):
    dist = 0
    if next_venue == 'CHI':
        dist = 5
    if team == 'MEL':
        if next_venue == 'MEL':
            dist = 0
        elif (next_venue == 'VIC'):
            dist = 1
        elif (next_venue == 'TAS' or next_venue == 'SYD'
            or next_venue == 'ACT' or next_venue == 'SA'):
            dist = 2
        elif (next_venue == 'WA' or next_venue == 'NZ'
            or next_venue == 'QLD'):
            dist = 3
        else:
            dist = 4

    if team == 'GEE':
        if next_venue == 'GEE':
            dist = 0
        elif (next_venue == 'VIC' or next_venue == 'MEL'):
            dist = 1
        elif (next_venue == 'TAS'or next_venue == 'SYD'
            or next_venue == 'ACT' or next_venue == 'SA'):
            dist = 2
        elif (next_venue == 'WA' or next_venue == 'NZ'
            or next_venue == 'QLD'):
            dist = 3
        else:
            dist = 4

    if team == 'SYD':
        if next_venue == 'SYD':
            dist = 0
        elif (next_venue == 'ACT'):
            dist = 1
        elif (next_venue == 'SA'or next_venue == 'VIC'
            or next_venue == 'QLD'or next_venue == 'MEL'):
            dist = 2
        elif (next_venue == 'TAS' or next_venue == 'NZ'
            or next_venue == 'NT' ):
            dist = 3
        else:
            dist = 4

    if team == 'ADE':
        if next_venue == 'SA':
            dist = 0
        elif (next_venue == 'VIC'or next_venue == 'SYD'
            or next_venue == 'ACT' or next_venue == 'TAS'
            or next_venue == 'MEL'):
            dist = 2
        elif (next_venue == 'QLD' or next_venue == 'WA'
            or next_venue == 'NT'):
            dist = 3
        else:
            dist = 4

    if team == 'QLD':
        if next_venue == 'QLD':
            dist = 1
        elif (next_venue == 'SYD' or next_venue == 'ACT'):
            dist = 2
        elif (next_venue == 'VIC' or next_venue == 'MEL'
            or next_venue == 'NT' or next_venue == 'SA'):
            dist = 3
        else:
            dist = 4

    if team == 'PER':
        if next_venue == 'WA':
            dist = 0
        elif (next_venue == 'SA' or next_venue == 'NT'):
            dist = 3
        else:
            dist = 4

    return dist