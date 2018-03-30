import foursquare

client = foursquare.Foursquare(client_id='1B2TR04AIROKCJV0DJ1IMGY1XNHZCJLSMOMZABV5WR4LZX4H', client_secret='GTNERYL0L3WMDUG2QSCNWLZCO30AFW1E4X3UMFXACT02L41M', redirect_uri='')
auth_uri = client.oauth.auth_url()

def search(category_id,num_results):
    search = client.venues.search(params={'ll': "41.634743, -80.154473", "limit": num_results, 'categoryId': category_id})
    venues = search['venues']
    for venue in venues:
         print(venue['name'])


def get_categories():
    categories = client.venues.categories()
    category_list = categories['categories']
    for category in category_list:
        print(category['name'])

def get_sub_categories():
    categories = client.venues.categories()
    category_list = categories['categories']
    for category in category_list:
        print(category['name'])
        for c in category['categories']:
            print("\t"+c['name'])
        print()

def get_category_id(c):
    categories = client.venues.categories()['categories']
    for category in categories:
        if c == category['name'].lower():
            return category['id']
        else:
            for cat in category['categories']:
                if c == cat['name'].lower():
                    return cat['id']
    return None

33768001254476
