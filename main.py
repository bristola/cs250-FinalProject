import main
import foursquareTest
import picker
from user import User

commands = ['quit','help','categories','search']
users = list()
if __name__ == '__main__':
    print("Insert project name here\n")
    command = str(input("What would you like to do\n")).lower()
    while command != "quit":
        if command == "help":
            main.help_info()
        elif command == "search":
            main.search()
        elif command == "categories":
            sub = str(input("Would you like to view sub categories as well (yes/no)\n")).lower()
            if sub == "no":
                foursquareTest.get_categories()
            else:
                foursquareTest.get_sub_categories()
        elif command == "new user":
            users.append(main.createUser())
        elif command == "show users":
            for u in users:
                print("test"+repr(u))
        elif command == "pick location":
            picker.pickLocation(users)

        command = str(input("\nWhat would you like to do\n")).lower()

def createUser():
    userID = input("What is the users ID?")
    city = None
    longitude = None
    latitude = None
    decision = input("Would you like to input a city or longitude/latitude? (1 or 2)")
    if decision == "1":
        city = input("What city do you live in?")
    elif decision == "2":
        longitude = input("What is your longitude?")
        latitude = input("What is your latitude?")
    user = User(userID, longitude, latitude, city)

    print("Please enter as many food intersts you want from the list of food interests (type stop if you are done entering interests)")
    foodInterests = list()
    while (True):
        interest = input().lower()
        if (interest == "stop"):
            break
        foodInterests.append(interest)
    for interest in list(foodInterests):
        category_id = foursquareTest.get_category_id(interest)
        if category_id == None:
            foodInterests.remove(interest)
    user.setFoodInterests(foodInterests)

    print("Please enter as many activity intersts you want from the list of activity intersts (type stop if you are done entering interests)")
    interests = list()
    while (True):
        interest = input().lower()
        if (interest == "stop"):
            break
        interests.append(interest)
    for i in list(interests):
        category_id = foursquareTest.get_category_id(i)
        if category_id == None:
            interests.remove(i)
    user.setInterests(interests)

    return user

def search():
    category = str(input("What category would you like to search\n")).lower()
    category_id = foursquareTest.get_category_id(category)
    if category_id == None:
        print("Category could not be found")
        return
    num_results = str(input("How many results would you like to see (Max: 100)\n"))
    foursquareTest.search(category_id, num_results)

def help_info():
    print("Possible Commands:")
    for command in commands:
        print("\t"+command)
    return
