import os
import time

def check_internet_connection():
    response = os.system("ping -c 1 google.com")
    return response == 0

def restart_network_manager():
    os.system("sudo service NetworkManager restart")
    time.sleep(20)

def main():
    while True:
        if not check_internet_connection():
            print("No internet connection. Restarting NetworkManager...")
            restart_network_manager()
        else:
            print("Internet connection is active.")
        
        time.sleep(10)

if __name__ == "__main__":
    main()
