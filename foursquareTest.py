import foursquare

client = foursquare.Foursquare(client_id='PLACEHOLDER', client_secret='PLACEHOLDER', redirect_uri='dslkfja')

auth_uri = client.oauth.auth_url()

search = client.venues.search(params={'ll': "41.634743, -80.154473", "limit": "50"})

venues = search['venues']

for venue in venues:
    print(venue['name'])

# print(str(test['venues']))
