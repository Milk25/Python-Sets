our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}


common_destinations = our_routes.intersection(competitor_routes)

unique_destinations = our_routes.difference(competitor_routes)

destinations_that_neither_airline_shares = our_routes.symmetric_difference(competitor_routes)

print("Destinations that both airlines fly to:", common_destinations)
print("Destinations unique to your airline:",unique_destinations)
print("Destinations that neither airlines shares:",destinations_that_neither_airline_shares)



