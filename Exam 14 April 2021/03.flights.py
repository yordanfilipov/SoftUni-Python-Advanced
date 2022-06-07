def flights(*args):
    initial_flights = [el for el in args]
    flights_dict = {}
    for i in range(0, len(initial_flights), 2):
        if initial_flights[i] == "Finish":
            return flights_dict
        if initial_flights[i] not in flights_dict:
            flights_dict[initial_flights[i]] = int(initial_flights[i+1])
        else:
            flights_dict[initial_flights[i]] += int(initial_flights[i+1])
    return flights_dict


print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))