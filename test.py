import user
import foursquareAPI
import picker

user1 = user.User(1, 'Albany', 'NY')
user2 = user.User(2, 'Latham', 'NY')
user3 = user.User(3, 'Colonie', 'NY')
user4 = user.User(4, 'Pittsburgh', 'PA')

user1.setFoodInterests(['diner'])
user2.setFoodInterests(['diner'])
user3.setFoodInterests(['diner'])
user4.setFoodInterests(['food court','irish pub'])

user1.setInterests(['movie theater','cemetery'])
user2.setInterests(['bar','cemetery'])
user3.setInterests(['gun range','pool'])
user4.setInterests(['park','bar'])

fVenues, aVenues = picker.pickLocations([user1])
picker.printLocations(fVenues,aVenues)
#print(foursquareAPI.get_venue_price(fVenues[0]))
# venues = foursquareAPI.search(user1,foursquareAPI.get_category_id('diner'))
# for venue in venues:
#     print(foursquareAPI.get_venue_location(venue))
