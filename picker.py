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

def pickLocations(ranksFood, ranks, venues):
    return
