import json
import os
import base64

FILE_NAME = "passwords.json"

# Encode password (basic, not secure for real-world use)
def encode_password(password):
    return base64.b64encode(password.encode()).decode()

# Decode password
def decode_password(encoded_password):
    return base64.b64decode(encoded_password.encode()).decode()

# Load saved data
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Add new credential
def add_password():
    site = input("Enter site name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    data = load_data()
    data[site] = {
        "username": username,
        "password": encode_password(password)
    }

    save_data(data)
    print("✅ Password saved successfully!")

# View all credentials
def view_passwords():
    data = load_data()
    if not data:
        print("No passwords saved.")
        return

    for site, creds in data.items():
        print(f"\n🌐 Site: {site}")
        print(f"👤 Username: {creds['username']}")
        print(f"🔑 Password: {decode_password(creds['password'])}")

# Search for a site
def search_password():
    site = input("Enter site name to search: ")
    data = load_data()

    if site in data:
        creds = data[site]
        print(f"\n🌐 Site: {site}")
        print(f"👤 Username: {creds['username']}")
        print(f"🔑 Password: {decode_password(creds['password'])}")
    else:
        print("❌ No record found.")

# Main menu
def main():
    while True:
        print("\n==== Password Manager ====")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Search Password")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()