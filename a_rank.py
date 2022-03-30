num_airport, num_flight = [int(num) for num in input().split(' ')]

airports = [airport + 1 for airport in range(num_airport)]

flights_dict = {}
for airport in airports:
    flights_dict[airport] = []
flights = []
for flight in range(num_flight):
    flight = [int(num) for num in input().split(' ')]
    flights.append(flight)
    flights_dict[flight[0]].append(flight)


def pass_all_ports(flights, airports):
    port_passed = []
    for flight in flights:
        port_passed.append(flight[1])
    port_passed = list(set(port_passed))
    if port_passed != airports:
        print('No')
        exit()

def no_duplicate(flights):
    existing_flights = []
    for flight in flights:
        flight = sorted(flight)
        if flight in existing_flights:
            print('No')
            exit()
        existing_flights.append(flight)


def sim_flight_init(flights):

    for flight in flights:
        next_port = flight[1]
        sim_flight_roop(flights, next_port)
    print('No')
    exit()



def sim_flight_roop(flights, next_port):
    port_passed = []
    for flight in flights:
        if flight[0] == next_port:
            next_port = flight[1]
            port_passed.append(next_port)
    if list(set(port_passed)) == airports:
        print('Yes')
        exit()


no_duplicate(flights)
pass_all_ports(flights, airports)
print('Yes')
# sim_flight_init(flights)
