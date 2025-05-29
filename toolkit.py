# toolkit.py
import port_scanner
import brute_forcer

def main():
    print("Penetration Testing Toolkit")
    print("1. Port Scanner")
    print("2. Brute Forcer")
    choice = input("Choose a tool to use (1/2): ")
    
    if choice == "1":
        target = input("Enter target IP or domain: ")
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))
        open_ports = port_scanner.scan_ports(target, start_port, end_port)
        if open_ports:
            print(f"Open ports: {open_ports}")
        else:
            print("No open ports found.")
    
    elif choice == "2":
        url = input("Enter the login URL: ")
        username = input("Enter the username: ")
        password_file = input("Enter path to password list file: ")

        try:
            with open(password_file, 'r') as file:
                password_list = file.readlines()

            brute_forcer.brute_force_login(url, username, [pwd.strip() for pwd in password_list])
        except FileNotFoundError:
            print("Password list file not found.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
