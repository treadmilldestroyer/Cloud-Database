import firebase_admin 
from firebase_admin import credentials, firestore

# This is the connection to the database
cred = credentials.Certificate("firestore-permissions.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# This script is for storing car information. In this script you will be able to:
# - add a new car
# - update a car
# - delete a car
# - query for a car

def add_new_car():
    print("\n--- Add New Data to Database ---")
    type = input("Enter the type of car(truck, sedan, suv, or van): ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    year = input("Enter the year: ")

    car_description = {
        "type": type,
        "make": make,
        "model": model,
        "year": year
    }

    update_time, doc_ref = db.collection("cars").add(car_description)
    print(f"\n✅ Success! Your car was added with ID: {doc_ref.id}")


def query_car():
    print("\n--- Query a Car ---")
    query_term = input("Enter the [type], [make], [model], or [year] of the car you are looking for: ")

    fields_to_search = ["type", "make", "model", "year"]
    results_found = False

    for field in fields_to_search:
        docs = db.collection("cars").where(field, "==", query_term).stream()

        for doc in docs:
            car = doc.to_dict()
            print(f"Based on your search [{field}] we found: ID {doc.id} -> {car['year']} {car['make']} {car['model']} {car['type']}")
            results_found = True
    
    if not results_found:
        print(f"No cars found matching '{query_term}'.")

def delete_car():
    print("\n--- Delete a Car ---")
    doc_id = input("Enter the Document ID of the car you want to delete: ")
    # Confirming that the user really wants to delete the car from the data base
    confirmation = input(f"Are you sure you want to delete car {doc_id}? (y/n): ")

    if confirmation.lower() == 'y':
        db.collection("cars").document(doc_id).delete() # this does the actual deleting from the db
        print(f"Car {doc_id} has been deleted from the database.")
    else:
        print("Delete cancelled.")

def main():
    while True:
        print("1. Add a car")
        print("2. Query a car")
        print("3. Exit menu")
        
        choice = input("What would you like to do? ")

        if choice == '1':
            add_new_car()
        elif choice == '2':
            query_car()
        elif choice == '3':
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()