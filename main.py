import main
import foursquareAPI
import picker
from user import User

commands = ['quit','help','categories','search','new user','show users','delete user','pick location']
users = list()
if __name__ == '__main__':
    print("Venue Picker\n")
    command = str(input("What would you like to do\n")).lower()
    while command != "quit":
        if command == "help":
            main.help_info()
        elif command == "search":
            main.general_search()
        elif command == "categories":
            sub = str(input("Would you like to view sub categories as well (yes/no)\n")).lower()
            if sub == "no":
                foursquareAPI.get_categories()
            else:
                foursquareAPI.get_sub_categories()
        elif command == "new user":
            users.append(main.createUser())
        elif command == "show users":
            if len(users) != 0:
                for u in users:
                    print(repr(u))
            else:
                print("No Users")
        elif command == "delete user":
            main.delete_user(users)
        elif command == "pick location":
            picker.pickLocations(users)
        else:
            print("That is not an option")

        command = str(input("\nWhat would you like to do\n")).lower()

def createUser():
    print("Please enter in user's information, enter cancel to cancel")
    userID = input("What is the users ID? ")
    if userID == "cancel":
        return
    city = None
    state = None
    city = input("What city do you live in? ")
    if city == "cancel":
        return
    state = input("What state is the city in? ")
    if state == "cancel":
        return
    user = User(userID, city, state)

    print("Please enter as many food intersts you want from the list of food interests (type stop if you are done entering interests, type cancel to cancel)")
    foodInterests = list()
    while (True):
        interest = input().lower()
        if (interest == "stop"):
            break
        if (interest == "cancel"):
            return
        foodInterests.append(interest)
    for interest in list(foodInterests):
        category_id = foursquareAPI.get_category_id(interest)
        if category_id == None:
            foodInterests.remove(interest)
    user.setFoodInterests(foodInterests)

    print("Please enter as many activity intersts you want from the list of activity intersts (type stop if you are done entering interests, type cancel to cancel) ")
    interests = list()
    while (True):
        interest = input().lower()
        if (interest == "stop"):
            break
        if (interest == "cancel"):
            return
        interests.append(interest)
    for i in list(interests):
        category_id = foursquareAPI.get_category_id(i)
        if category_id == None:
            interests.remove(i)
    user.setInterests(interests)

    return user

def delete_user(users):
    userID = input("What userId would you like to delete? ")
    for user in list(users):
        if user.getId() == userID:
            users.remove(user)

def general_search():
    category = str(input("What category would you like to search\n")).lower()
    category_id = foursquareAPI.get_category_id(category)
    if category_id == None:
        print("Category could not be found")
        return
    num_results = str(input("How many results would you like to see (Max: 50)\n"))
    foursquareAPI.general_search(category_id, num_results)

def help_info():
    print("Possible Commands:")
    for command in commands:
        print("\t"+command)
    return
