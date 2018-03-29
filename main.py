import main
import foursquareTest

commands = ['quit','help','categories','search']
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

        command = str(input("\nWhat would you like to do\n")).lower()

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
