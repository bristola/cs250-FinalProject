class User:

    userID = None
    foodInterests = None
    interests = None
    lon = None
    lat = None
    city = None

    def __init__(self, userID, lon=None, lat=None, city=None):
        self.userID = userID
        self.foodInterests = list()
        self.interests = list()
        self.lon = lon
        self.lat = lat
        self.city = city

    def getLongitude(self):
        return self.lon

    def getLatitude(self):
        return self.lat

    def getCity(self):
        return self.city

    def getFoodInterests(self):
        return self.foodInterests

    def getInterests(self):
        return self.interests

    def setLongitude(self, lon):
        self.lon = lon

    def setLatitude(self, lat):
        self.lat = lat

    def setFoodInterests(self, foodInterests):
        self.foodInterests = foodInterests

    def setInterests(self, interests):
        self.interests = interests

    def __repr__(self):
        return str(self.userID) + " | " + str(self.city)+" | " + str(self.lon) + " " + str(self.lat) + " | " + "Food Interests: "+ ' '.join(self.foodInterests) + " | " + "Interests: "+ ' '.join(self.interests)
