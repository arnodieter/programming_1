from trip import trip
def add_trip():
    destination = input("Please enter the destination of your trip: ")
    starting_date = input("Please enter the starting date of your trip: ")
    end_date = input("Please enter the end date of your trip: ")
    amount_of_trouser = input("Please enter the amount of trousers of your trip: ")
    add_new_trip = trip(destination, starting_date, end_date, amount_of_trouser)
    trip_list.append(add_new_trip)


def list_trip():
    print("\n"*100)
    for trip in trip_list:
        print("Destination: " + trip.destination)
        print(f"Starting date: {trip.starting_date}")
        print(f"Ending date: {trip.end_date}")
        print(f"Amount of trousers of your trip: {trip.amount_of_trouser}\n")



def store_trips():
    with open("trips.txt", 'w', encoding='utf-8') as f:
        for trip in trip_list:
            f.write(f"{trip.destination};")
            f.write(f"{trip.starting_date};")
            f.write(f"{trip.end_date};")
            f.write(f"{trip.amount_of_trouser};\n")


def restore_trips():
    with open("trips.txt", 'r', encoding='utf-8') as f:
        for line in f.readlines():
            fields = line.split(";")
            trip_list.append(trip(fields[0], fields[1], fields[2], fields[3]))


def full_text_search(user_search):
    print("\n"*100)
    for trip in trip_list:
        if user_search.lower() in trip.to_string().lower():
            print(f"Destination: {trip.destination}")
            print(f"Starting date: {trip.starting_date}")
            print(f"Ending date: {trip.end_date}")
            print(f"Amount of trousers of your trip: {trip.amount_of_trouser}\n")

def delete_trip(delete):
    print("\n" * 100)
    for index, trip in enumerate(trip_list):
        if delete.lower() in trip.to_string().lower():
            print(index)
            print(f"Destination: {trip.destination}")
            print(f"Starting date: {trip.starting_date}")
            print(f"Ending date: {trip.end_date}")
            print(f"Amount of trousers of your trip: {trip.amount_of_trouser}\n")
    delete_option = input("which one you want to delete: ")
    try:
        deleted_item = trip_list.pop(int(delete_option))
        print(f"deleted {deleted_item.destination} trip")
    except IndexError:
        print("Wrong input")

def export_trip():
    with open("exp.txt", 'w', encoding='utf-8') as f:
        for trip in trip_list:
            f.write(f"Destination: {trip.destination}\n")
            f.write(f"Starting date: {trip.starting_date}\n")
            f.write(f"End date: {trip.end_date}\n")
            f.write(f"Amount of trousers: {trip.amount_of_trouser}\n\n")

trip_list = []


try:
    restore_trips()
except:
    print("Cant open the file")
while True:
    print("Main Menu")
    print("What do you want to do next?")
    print("1. Add a new trip")
    print("2. List all trips")
    print("3. Read all trips from file")
    print("4. Save the data")
    print("5. Find the data")
    print("6. Delete trip")
    print("7. Export trips")
    print("x. Exit the program")
    option = input("Your selection: ")
    if (option == "1"):
        add_trip()
    elif (option == "2"):
        list_trip()
    elif (option == "3"):
        restore_trips()
    elif (option == "4"):
        store_trips()
    elif (option == "5"):
        full_text_search(input("Please provide the search string: "))
    elif (option == "6"):
        delete_trip(input("Please provide the search string: "))
    elif (option == "7"):
        export_trip()
    elif (option.lower() == "x"):
        store_trips()
        quit()
    else:
        print("Bad output")











