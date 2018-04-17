class User:

    userID = None
    foodInterests = None
    interests = None
    city = None
    state = None

    def __init__(self, userID, city=None, state=None):
        self.userID = userID
        self.foodInterests = list()
        self.interests = list()
        self.city = city
        self.state = state

    def getId(self):
        return self.userID

    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getFoodInterests(self):
        return self.foodInterests

    def getInterests(self):
        return self.interests

    def setCity(self, city):
        self.city = city

    def setState(self, state):
        self.state = state

    def setFoodInterests(self, foodInterests):
        self.foodInterests = foodInterests

    def setInterests(self, interests):
        self.interests = interests

    def __repr__(self):
        return str(self.userID) + " | " + str(self.city)+", "+ str(self.state)+" | " + "Food Interests: "+ ' '.join(self.foodInterests) + " | " + "Interests: "+ ' '.join(self.interests)
