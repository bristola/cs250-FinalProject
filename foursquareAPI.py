import foursquare

api = foursquare.Foursquare(client_id='C5XWD1C35ATN44D2P2CQ0EIYOUP1FSDGFLXJJOQMU5CXNH3Y', client_secret='QACPAZY0ZHAAMBPM05OHS5NRJ5XD0ORMK0T23JZIKKGLTOAS', redirect_uri='')
auth_uri = api.oauth.auth_url()

def general_search(city,state,category_id,num_results):
    search = api.venues.search(params={'near': str(city)+","+str(state), "limit": num_results, 'categoryId': category_id, 'radius': '16000', 'intent': 'browse'})
    venues = search['venues']
    for venue in venues:
         print(venue['name'])

def search(user,cat):
    search = api.venues.search(params={'near': str(user.getCity())+","+str(user.getState()),'limit': '10', 'categoryId': str(cat), 'radius': '16000', 'intent': 'browse'})
    venues = search['venues']
    return venues

def get_venue_details(venue):
    return api.venues(venue)['venue']

def get_venue_location(venue):
    location = get_venue_details(venue['id'])['location']
    return location['formattedAddress']

def get_categories():
    categories = api.venues.categories()
    category_list = categories['categories']
    for category in category_list:
        print(category['name'])

def get_sub_categories():
    categories = api.venues.categories()
    category_list = categories['categories']
    for category in category_list:
        print(category['name'])
        for c in category['categories']:
            print("\t"+c['name'])
        print()

def get_category_id(c):
    categories = api.venues.categories()['categories']
    for category in categories:
        if c == category['name'].lower():
            return category['id']
        else:
            for cat in category['categories']:
                if c == cat['name'].lower():
                    return cat['id']
    return None
