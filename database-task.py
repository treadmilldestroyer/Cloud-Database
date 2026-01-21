import firebase_admin 
import pyrebase
import getpass
from firebase_admin import credentials, firestore

# This is the connection to the database
cred = credentials.Certificate("firestore-permissions.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# this is the handshake with Firebase and specific users and their emails
config = {
    "apiKey": "AIzaSyD1d8v5TzglpJKlSUJcfvq_lMBcMLaAJTc",
    "authDomain": "cse310-cloud-database.firebaseapp.com",
    "projectId": "cse310-cloud-database",
    "storageBucket": "cse310-cloud-database.firebasestorage.app",
    "messagingSenderId": "423935572575",
    "appId": "1:423935572575:web:2f9f6d587f2789396539ea",
    "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

# this allows users that have access to the database to login so they have access to the program
def login():
    email = input("Email: ")
    password = getpass.getpass("Password: ") # keeps password secret when typing them in

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("\n🔓 Success! Logged in as", user['email'])
        return True
    except:
        print(f"🔒 Login Failed. Check your email/password. \n")
        return False

# This script is for storing car information. In this script you will be able to:
# - add a new car
# - update a car
# - delete a car
# - query for a car

# this function adds a new document or piece of data with the 4 fields we're using in this car database
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
    print(f"\n✅ Success! Your car was added with ID: {doc_ref.id} TIME: {update_time}")

# this function is to search or query for a car
def query_car():
    print("\n--- Query a Car ---")
    # we're letting the user know what they can search for
    query_term = input("Enter anything (type, make, model, or year) of the car you are looking for: ")

    # here are the 4 fields the user can search for in the database
    fields_to_search = ["type", "make", "model", "year"]
    results_found = False

    for field in fields_to_search:
        # the .where() allows us to search for that query_term in the entire database
        docs = db.collection("cars").where(field, "==", query_term).stream()
        # if there is a query_term found, it will become a doc in the docs
        for doc in docs:
            car = doc.to_dict()
            print(f"Based on your search [{field}] we found: ID {doc.id} -> {car['year']} {car['make']} {car['model']} {car['type']}")
            results_found = True

    # Error Statement in the case that the car searched for is NOT in database
    # this error statement will be specific for the query_term used to search for
    if not results_found:
        print(f"No cars found matching '{query_term}'.")

# this function is to delete a car and its contents from database
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

# this function is used to update the contents of each car in the database
def update_car():
    doc_id = input("Enter the Document ID of the car you want to update: ")

    updates = {}
    
    while True:
        choice = input("Please select what you would like to update [year], [make], [model], [type]: ").lower()

        if choice in ['year', 'make', 'model', 'type']:
            new_value = input(f"Enter the new {choice}: ")
            updates[choice] = new_value
        else:
            print("Invalid selection.")

        again = input("Would you like to update another item?(y/n) ")
        if again != 'y':
            break

    if updates:
        try:
            db.collection("cars").document(doc_id).update(updates)
            print(f"✅ Successfully updated {list(updates.keys())} for car {doc_id}.")
        except Exception as e:
            print(f"Error: Could not find a car with ID '{doc_id}'.")

# main() creates a menu and uses the functions above to use database
def main():
    while True:
        if login():
            break

    while True:
        print("\n----- MENU -----")
        print("1. Add a car")
        print("2. Query a car")
        print("3. Delete a car")
        print("4. Update a car")
        print("5. Exit")
        
        choice = input("What would you like to do? ")

        if choice == '1':
            add_new_car()
        elif choice == '2':
            query_car()
        elif choice == '3':
            delete_car()
        elif choice == '4':
            update_car()
        elif choice == '5':
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()