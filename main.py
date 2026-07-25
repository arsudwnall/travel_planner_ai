from models.request import TripRequest

def main():
    trip = TripRequest(
        destination="Japan",
        days=5,        # try a negative number -> validation error
        budget=100000,  # try a negative number -> validation error
        travel_style="Luxury"
    )
    #print(trip)
    #print(trip.model_dump())          # convert to dictionary
    print(trip.model_dump_json(indent=2))  # convert to JSON

if __name__ == "__main__":
    main()