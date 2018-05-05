import user
import foursquareAPI
import picker

user1 = user.User(1, 'Albany', 'NY')
user2 = user.User(2, 'Latham', 'NY')
user3 = user.User(3, 'Colonie', 'NY')

user1.setFoodInterests(['diner'])
user2.setFoodInterests(['diner'])
user3.setFoodInterests(['diner'])

user1.setInterests(['movie theater'])
user2.setInterests(['bar'])
user3.setInterests(['gun range','pool'])

fVenues, aVenues = picker.pickLocations([user1])
picker.printLocations(fVenues,aVenues)
