# Counties of Ireland
counties = {
    'Antrim': 'AM',
    'Armagh': 'AH',
    'Carlow': 'CW',
    'Cavan': 'CN',
    'Clare': 'CE',
    'Cork': 'CK',
    'Derry': 'DY',
    'Donegal': 'DL',
    'Down': 'DN',
    'Dublin': 'D',
    'Fermanagh': 'FH',
    'Galway': 'GY',
    'Kerry': 'KY',
    'Kildare': 'KE',
    'Kilkenny': 'KY',
    'Laois': 'LS',
    'Leitrim': 'LM',
    'Limerick': 'LK',
    'Longford': 'LD',
    'Louth': 'LH',
    'Mayo': 'MO',
    'Meath': 'MH',
    'Monaghan': 'MN',
    'Offaly': 'OY',
    'Roscommon': 'RN',
    'Sligo': 'SO',
    'Tipperary': 'TY',
    'Tyrone': 'TE',
    'Waterford': 'WD',
    'Westmeath': 'WH',
    'Wexford': 'WX',
    'Wicklow': 'WW'
}

cities = {
    'AM': 'Ballymena',
    'AH': 'Armagh',
    'CW': 'Carlow',
    'CN': 'Cavan',
    'CE': 'Ennis',
    'CK': 'Cork',
    'DY': 'Derry',
    'DL': 'Lifford',
    'DN': 'Downpatrick',
    'D': 'Dublin',
    'FH': 'Enniskillen',
    'GY': 'Galway',
    'KY': 'Tralee',
    'KE': 'Naas',
    'KY': 'Kilkenny',
    'LS': ' Portlaoise',
    'LM': 'Carrick-on-Shanon',
    'LK': 'Limerick',
    'LD': 'Longford',
    'LH': 'Dundalk',
    'MO': 'Castlebar',
    'MH': 'Navan',
    'MN': 'Monaghan',
    'OY': 'Tullamore',
    'RN': 'Roscommon',
    'SO': 'Sligo',
    'TY': 'Nenagh',
    'TE': 'Omagh',
    'WD': 'Dungarvan',
    'WH': 'Mullingar',
    'WX': 'Wexford',
    'WW': 'Wicklow'
}

print '-' * 20

print len(counties.keys())

for county, abbrev in counties.items():
    print "%s is abbrevated %s" % (county, abbrev)


print '-' * 20

for abbrev, city in cities.items():
    print "%s has the town %s" % (abbrev, city)

print '-' * 20

for county, abbrev in counties.items():
    print "%s is abbrevated %s and has the town %s" % (
    county, abbrev, cities[abbrev]
    )
