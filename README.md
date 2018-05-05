# Final Project
## CMPSC 250
### Team 6
### Austin Bristol and Zachary Andrews

- - - -

## Running the Code

1. Traverse to the root directory of the project
2. Install FoursquareAPI with `pip3 install foursquare --user`
3. Run with `python3 main.py`

### There are eight different commands that you can enter:
    1. quit: exits the program
    2. help: displays all available commands
    3. categories: lists all the categories a user can enter as an interest
    4. search: allows you to manually search for venues in any area you'd like
    5. new user: prompts user to enter different information on a user that is attending the event
    6. show users: displays all users that have been added
    7. delete user: allows you to remove a user if they are no longer attending the envent
    8. pick location: executes the picker algorithm that picks locations based on the users interests

- - - -

## Pick Location Algorithm

This algorithm will rank the interests input by the users based on the number of
occurences each of the categories has. This uses a hashtable data structure to
more efficiently access and update the values. This is a O(n) operation which is
based on the number of interests the user input. Next it searches for the venues
using the Foursquare API, and then sort the locations it finds based on their
price. This sorting use the Quicksort algorithm, which makes this a O(nlogn)
complexity, where n is the number of venues where are search for.

This algorithm's implementation can be found in the picker.py file.

## Main

This just holds the code which excepts user input on what the user wants to do. Each of the commands that are found above are handled by this code. This functionality can be found in the main.py file.

## User

The user.py file just contains the object class for a user, which is just an
object which holds the different values such as interests, name, and location.

## Foursquare API

All the necessary functions that are used to connect with the foursquare backend and make requests can be found in the foursquareAPI.py file. These functions are used in both the main.py file as well as the picker.py file.
