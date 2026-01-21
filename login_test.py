import pyrebase

# this is the handshake with Firebase and specific users and their emails
config = {
    "apiKey": "AIzaSyD1d8v5TzglpJKlSUJcfvq_lMBcMLaAJTc",
    "authDomain": "cse310-cloud-database.firebaseapp.com",
    "projectId": "cse310-cloud-database",
    "storageBucket": "cse310-cloud-database.firebasestorage.app",
    "messagingSenderId": "423935572575",
    "appId": "1:423935572575:web:2f9f6d587f2789396539ea"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

def sign_in():
    email = input("Email: ")
    password = input("Password: ")

    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print("\n🔓 Success! Logged in as", user['email'])
        return user['idToken']
    except Exception as e:
        print(f"🔒 Login Failed. Check your email/password. \n{e}")

if __name__ == "__main__":
    sign_in()