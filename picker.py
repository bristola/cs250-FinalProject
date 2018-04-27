import foursquareAPI
import sort

def rankInterests(users):
    # Rank categories based on occurence
    maxFood = 0
    maxRank = 0
    ranksFood = dict()
    ranks = dict()
    for user in users:
        for food in user.getFoodInterests():
            if food in ranksFood:
                ranksFood[food] = ranksFood[food] + 1
            else:
                ranksFood[food] = 1
            if (ranksFood[food] > maxFood):
                maxFood = ranksFood[food]
        for interest in user.getInterests():
            if interest in ranks:
                ranks[interest] = ranks[interest] + 1
            else:
                ranks[interest] = 1
            if (ranks[interest] > maxRank):
                maxRank = ranks[interest]

    foodInterests = list()
    for key, value in ranksFood.items():
        if (value >= maxRank):
            foodInterests.append(key)

    interests = list()
    for key, value in ranks.items():
        if (value >= maxRank):
            interests.append(key)


    return foodInterests, interests

def pickLocations(users):
    food_venues = list()
    act_venues = list()
    food = ''
    other = ''
    maxFood, maxOther = rankInterests(users)
    for Food in maxFood:
        food += foursquareAPI.get_category_id(Food) + ','
    for Other in maxOther:
        other += foursquareAPI.get_category_id(Other) + ','
    for user in users:
        for venue in foursquareAPI.search(user,food):
            if venue not in food_venues:
                food_venues.append(venue)
        for venue in foursquareAPI.search(user,other):
            if venue not in act_venues:
                act_venues.append(venue)
    food_venues = sort.sort(food_venues,0,len(food_venues)-1)
    num = 1
    print("\n"+str(len(food_venues))+" Food Locations Sorted by Price:")
    for venue in food_venues:
        print(str(num)+": "+str(venue['name'])+"- "+str(foursquareAPI.get_venue_location(venue)))
        num+=1
    num = 1
    #act_venues = sort.sort(act_venues,0,len(act_venues)-1)
    print("\n"+str(len(act_venues))+" Activities:")
    for venue in act_venues:
        print(str(num)+": "+str(venue['name'])+"- "+str(foursquareAPI.get_venue_location(venue)))
        num+=1
    return food_venues, act_venues
