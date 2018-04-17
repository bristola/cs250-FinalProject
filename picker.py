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

    #for key, value in ranks.items():
        #print(str(key) +" : "+str(value))
    #print(str(list(ranksFood.keys())) +" "+ str(list(ranks.keys())))
    return list(ranksFood.keys()), list(ranks.keys())

def pickLocations(users):
    food_venues = list()
    act_venues = list()
    food = ''
    other = ''
    maxFood, maxOther = rankInterests(users)
    for Food in maxFood:
        food += foursquareTest.get_category_id(Food) + ','
    for Other in maxOther:
        other += foursquareTest.get_category_id(Other) + ','
    for user in users:
        for venue in foursquareTest.search(user,food):
            if venue not in food_venues:
                print("TEST1")
                food_venues.append(venue)
            else:
                print("TEST3")
        for venue in foursquareTest.search(user,other):
            if venue not in act_venues:
                print("TEST2")
                act_venues.append(venue)
            else:
                print("TEST4")
    num = 1
    print("\n"+str(len(food_venues))+" FOOD:")
    for venue in food_venues:
        print(str(num)+": "+venue['name'])
        num+=1
    num = 1
    print("\n"+str(len(act_venues))+" Activities:")
    for venue in act_venues:
        print(str(num)+": "+venue['name'])
        num+=1
    return
