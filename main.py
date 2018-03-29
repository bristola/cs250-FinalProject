import foursquareTest

commands = ['quit','help','categories','search']
if __name__ == '__main__':
    print("Insert project name here\n")
    command = str(input("What would you like to do\n")).lower()
    while command != "quit":
        if command == "help":
            help_info()
        elif command == "search":
            foursquareTest.search()
        elif command == "categories":
            sub = str(input("Would you like to view sub categories as well (yes/no)\n")).lower()
            if sub == "no":
                foursquareTest.get_categories()
            else:
                foursquareTest.get_sub_categories()

        command = str(input("\nWhat would you like to do\n")).lower()


def help_info():
    print("Possible Commands:\n")
    for command in commands:
        print(command)
