import foursquareAPI

def sort(venues, p, r):
    if len(venues) == 0:
        return None
    if p < r:
        q = partition(venues,p,r)
        sort(venues,p,q-1)
        sort(venues,q+1,r)
    return venues

def partition(venues, p, r):
    x = venues[r]
    i = p - 1
    for j in range(p, r):
        if foursquareAPI.get_venue_price(venues[j]) > foursquareAPI.get_venue_price(venues[j]):
            i = i + 1
            temp = venues[i]
            venues[i] = venues[j]
            venues[j] = temp
    temp = venues[i+1]
    venues[i+1] = venues[r]
    venues[r] = temp
    return i+1
