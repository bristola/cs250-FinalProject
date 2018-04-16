import foursquareTest
def rankInterests(users):
    # Rank categories based on occurence
    ranksFood = dict()
    for user in users:
        for food in user.getFoodInterests():
            if food in ranksFood:
                ranksFood[food] = ranksFood[food] + 1
            else:
                ranksFood[food] = 1

    ranks = dict()
    for user in users:
        for interest in user.getInterests():
            if interest in ranks:
                ranks[interest] = ranks[interest] + 1
            else:
                ranks[interest] = 1

    for key, value in ranks.items():
        print(str(key) +" : "+str(value))
    print(str(list(ranksFood.keys())) +" "+ str(list(ranks.keys())))
    return list(ranksFood.keys()), list(ranks.keys())

def pickLocations(users):
    food = ''
    other = ''
    maxFood, maxOther = rankInterests(users)
    for Food in maxFood:
        food += foursquareTest.get_category_id(Food) + ','
    for Other in maxOther:
        other += foursquareTest.get_category_id(Other) + ','
    picked = list()
    print(len(users))
    for user in users:
        venues = foursquareTest.search(user,food,other)
        # for venue in list(venues):
        #     if maxFood not in venue['categories'] or maxOther not in venue['categories']:
        #         venues.remove(venue)
        for venue in venues:
            picked.append(venue)
    print("\nPicked: ")
    for pick in picked:
        print(pick['name'])
    return
