import foursquare

api = foursquare.Foursquare(client_id='LCC353M4TCQFYV1TTYMKHQ40SLHSHZC5DHFVUGB0QC2DQNTH', client_secret='ZJ0XMHGIMT5IOORPDHVQAUH0NS3M04DOTFM2FEYJLCGARUPW', redirect_uri='')
auth_uri = api.oauth.auth_url()

def general_search(city,state,category_id,num_results):
    search = api.venues.search(params={'near': str(city)+","+str(state), "limit": num_results, 'categoryId': category_id})
    venues = search['venues']
    for venue in venues:
         print(venue['name'])

def search(user,food,other):
    print()
    search_food = api.venues.search(params={'near': str(user.getCity())+","+str(user.getState()), 'categoryId': str(food)})
    # print("test\n"+ str(search_food) + "\ntest")
    search_other = api.venues.search(params={'near': str(user.getCity())+","+str(user.getState()), 'categoryId': str(other)})
    for venue in search['venues']:
        print(venue)
        for categories in venue['categories']:
            print("\t"+str(categories))
    venues = search['venues']
    # for venue in venues:
    #     print(venue['name'])
    return venues

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
