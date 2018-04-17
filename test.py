import user
import foursquareTest
import picker

user1 = user.User(1, 'Albany', 'NY')
user2 = user.User(2, 'Latham', 'NY')
user3 = user.User(3, 'Meadville', 'PA')
user4 = user.User(4, 'Pittsburgh', 'PA')

user1.setFoodInterests(['diner'])
user2.setFoodInterests(['diner'])
user3.setFoodInterests(['buffet','burger joint'])
user4.setFoodInterests(['food court','irish pub'])

user1.setInterests(['movie theater','cemetary'])
user2.setInterests(['cemetary','bar'])
user3.setInterests(['gun range','pool'])
user4.setInterests(['park','bar'])

picker.pickLocations([user1,user2])
