# Car Dealership Cloud Database Software

This project is a program desinged to work alongside Google Firebase. The user will be able to add, delete, query, and update a database for a car dealership. Before the program enters the main menu with the 4 options to edit the database, the user must authenticate by logging in. Then whatever the user does will connect to the database in Firebase.

## Instructions for Build and Use

[My Software Demo](https://youtu.be/GqTf_BtAGPY)

Steps to build and/or run the software:

1. Log in with an existing user's credentials
2. Choose whatever action you would like to perform. 
3. Enter 5 to exit program.

Instructions for using the software:

To add a car to the database:
1. From main menu, press '1'.
2. Enter the type, make, model, and year each followed by 'enter' to move to the next detail.

To query a car from the database:
1. From main menu, press '2'.
2. Enter the type of detail you want to query by.

To delete a car from the database:
1. In order to delete a car, you'll first need the ID of the document from the database.
2. My recommendation to to first perform a query of the car you want to delete, and copy the ID.
3. Once you have the ID of the document you want to delete, from the main menu, press '3'. 
4. Enter the ID of the document you want to delete.
5. You will be prompted with a confirmation that you want to delete the document, enter 'y' for yes, and 'n' for no.

To update a car's details from the database:
1. In order to update a car's details, you'll first need the ID of the document from the database.
2. My recommendation to to first perform a query of the car you want to update, and copy the ID.
3. Enter the detail('type', 'make', 'model', or 'year') that you want to update.
4. Enter the updated info.
5. You'll be asked if you'd like to make another update, enter 'y' for yes, and 'n' for no.
6. You'll be stuck in the update function until you confirm with a 'n' that you don't want to make another update.

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Google Firebase
* VS Code
* Python (3.11.5)
* Libraries: firebase_admin, pyrebase, and getpass

## Useful Websites to Learn More

I found these websites useful in developing this software:

* [Google Firebase Documentation](https://firebase.google.com/docs?authuser=0)
* [Google Gemini](https://gemini.google.com/u/0/app)


## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* [ ] Add a GUI to this program.
* [ ] Have MFA for user authentication.
* [ ] Add a link to the Firebase console to make additional adjustments to the database that cannot be performed on program. 