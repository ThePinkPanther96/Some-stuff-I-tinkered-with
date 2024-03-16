import datetime as dt
import math
import os
import pickle
import sys
from time import sleep

from colorama import Fore

# Create data file 
parking = db = None
def save_parking():
    global parking, db
    if parking is None or db is None:
        return
    with open(db, 'wb') as file:
        pickle.dump(parking, file)


class Car:
    def __init__(self, license_number, phone_number, car_type, arrival=None):
        self.license_number = license_number
        self.phone_number = phone_number
        self.car_type = car_type
        self.arrival = arrival or dt.datetime.now()


    def __str__(self):
        return (f"{Fore.WHITE}Licesnse number: {Fore.LIGHTYELLOW_EX}{self.license_number} {Fore.WHITE}| Phone number: {Fore.LIGHTYELLOW_EX}{self.phone_number} {Fore.WHITE}| Car type: {Fore.LIGHTYELLOW_EX}{self.car_type} " 
        + str(f"{Fore.WHITE}| Arrival time: {Fore.LIGHTYELLOW_EX}{self.arrival.strftime('%d-%m-%Y %H:%M')}"))

    def __eq__(self, other):  # equal to
        return self.license_number == other.license_number  # in / not in


class ParkingLot:
    def __init__(self, price_per_hour=None, maximum_capacity=20, price_per_day=None):
        self.lot = dict()
        self.__price_per_day = price_per_day
        self.__price_per_hour = price_per_hour
        self.__maximum_capacity = maximum_capacity

    #  set & get for admin
    def get_price_per_day(self):
        return self.__price_per_day

    def set_price_per_day(self, price_per_day):
        self.__price_per_day = price_per_day
    
    def get_price_per_hour(self):
        return self.__price_per_hour
    
    def set_price_per_hour(self, price_per_hour):
        self.__price_per_hour = price_per_hour

    def get_maximum_capacity(self):
        return self.__maximum_capacity

    def set_maximum_capacity(self, maximum_capacity):    
        self.__maximum_capacity = maximum_capacity     


    def add_car(self, license_number, phone_number, car_type):
        if license_number in self.lot or len(self.lot) >= self.__maximum_capacity:
            return False
        self.lot[license_number] = Car(license_number, phone_number, car_type)
        return True

    
    def print_cars_above_24_hours(self):
        print("    All Cars In Lot More than 24 hours    ".center(120, '='))
        to_print = []
        for c in self.lot.values():
            if dt.datetime.now() - c.arrival > dt.timedelta(hours=24):
                to_print.append(str(c).center(120, '-'))
        if to_print:
            print('\n'.join(to_print))
        else:
            print(Fore.RED + "No cars parking over 24 hours")

    
    def calculate_price(self, license_number):
        if license_number not in self.lot:
            return 0
        car = self.lot[license_number]
        time_in_the_lot = dt.datetime.now() - car.arrival
        if time_in_the_lot < dt.timedelta(minutes=0):
            return 0
        if time_in_the_lot.days > 1:
            return time_in_the_lot.days * self.__price_per_day

        hours = math.ceil(time_in_the_lot.seconds / 3600)
        if hours * self.__price_per_hour > self.__price_per_day:
            return self.__price_per_day
        return hours * self.__price_per_hour

    def remove_car(self, license_number):
        if license_number in self.lot:
            del self.lot[license_number]
            return True
        return False

    def print_cars_in_lot(self):
        print(Fore.WHITE + "    All Cars In Lot    ".center(120, '='))
        for c in self.lot.values():
            print(str(c).center(100, '-'))
    
    def avalble_space_in_lot(self):
        amount_the_cars_left = self.__maximum_capacity - len(self.lot)
        return amount_the_cars_left
    
    def reset_lot(self):
        self.lot.clear()
        print(f"{Fore.GREEN}Parking lot cleared.")

####################################################################################
####################################  FUNCTIONS  ###################################
####################################################################################

# Password Policy:
def password_policy():
    name = "admin"
    passowrd = "admin"
    counter = 1

    while True:
        if counter > 3:
            print(Fore.RED + "To many faild logins! going back to main menu.")
            return False
        try:
            username = input(str(Fore.WHITE + "Please enter admin username: "))
        except (ValueError, TypeError):
            print(Fore.RED + f"Oops :-( Invalid Input!")
            continue
        if username != name:
            print(Fore.RED + f"Username not recodnized! Please enter a valid username")
            counter += 1
            continue
        try:
            usrpsswd = input("Please enter admin password: ")
        except (ValueError, TypeError):
            print(Fore.RED + f"Oops :-( Invalid Input!")
            continue
        if usrpsswd != passowrd:
            print(Fore.RED + f"Invalid Password! Please enter a valid password!")
            counter += 1
            continue
        break

    return True


def get_car_details_from_user():
    print(Fore.LIGHTBLACK_EX + "Price per hour: ", parking.get_price_per_hour())
    print(Fore.LIGHTBLACK_EX + "Free parking space: ", parking.avalble_space_in_lot())
    if parking.avalble_space_in_lot() < 1:
        sleep(1)
        print(Fore.RED + "Parking lot is full!")
        return
    print(f"{Fore.WHITE}Please enter the following information:\n ")

    while True:
        car_number = input(Fore.WHITE + "Enter car license number: ")
        if len(car_number) < 7 or len(car_number) > 8:
            print(Fore.RED + "Please enter a valid license number!")
            continue
        if car_number.isnumeric():
            save_car_number_as_israeli_number = f"{car_number}"
            break
        else:
            print(Fore.RED + "License number must include only numbers!")

    while True:
        phone_number = input(Fore.WHITE + "Enter phone number: ")
        if len(phone_number) == 10:
            if phone_number.isnumeric():
                save_number_as_israeli_number = f"{phone_number[:3]}-{phone_number[3:]}"
                break
            else:
                print(Fore.RED + "Phone number must in include only numbers!")
        else:
            print(Fore.RED + "Phone number must includs 10 numbers!")

    while True:
        print(f"""
        {Fore.WHITE}Choose car type:
        {Fore.LIGHTBLACK_EX}1. Private 
        {Fore.LIGHTBLACK_EX}2. Commercial
        {Fore.LIGHTBLACK_EX}3. Public
        """)
        car_type = input(Fore.  WHITE + "Choose car type: ")
        if car_type == "1":
            result_of_car_type = "Private"
            break
        if car_type == "2":
            result_of_car_type = "Commercial"
            break
        if car_type == "3":
            result_of_car_type = "Public"
            break
        else:
            print(Fore.RED + "Invalide input! Please enter a valid option.")
            continue

    if parking.add_car(save_car_number_as_israeli_number, save_number_as_israeli_number, result_of_car_type) is True:
        parking.print_cars_in_lot()
    else:
        parking.print_cars_in_lot()


def get_car_to_remove():
    while True:
        try:
            car_number = input(str(f"{Fore.WHITE}Please Enter License number: {Fore.YELLOW}"))
        except (ValueError, TypeError):
            print(f"{Fore.RED}Oops :-( Invalid Input!")
            sleep(0.5)
            continue
        if car_number in parking.lot:
            price_to_pay = parking.calculate_price(car_number)
            if price_to_pay == 0:
                parking.remove_car(car_number)
                print(f"{Fore.GREEN}Car exited successfully!")
                sleep(1)
                break
            try:
                payment = int(input(f"""{Fore.RED}Please provid {price_to_pay}$:{Fore.WHITE} """))
            except (ValueError, TypeError):
                print(f"{Fore.RED}Oops :-( Invalid Input!")
                sleep(0.5)
                continue
            while payment < price_to_pay:
                try:
                    payment = int(input(f"""{Fore.RED}Need to provid at least {price_to_pay}$:{Fore.WHITE} """))
                except (TypeError, ValueError):
                    print(f"{Fore.RED}Oops :-( Invalid Input!")
                    sleep(0.5)
                    continue   
            sleep(0.5)
            print(f"{Fore.YELLOW}the change is {payment - price_to_pay}")
            sleep(0.5)
            print(f"{Fore.GREEN}Car exited successfully!")
            parking.remove_car(car_number)
            break
        else:
            print(f"{Fore.RED}License number not found!")
            sleep(0.5)
            continue
    
def set_price_per_day():
    while True:
        print(Fore.LIGHTBLACK_EX + "Current price per day: ", parking.get_price_per_day())
        new_price = input((f"{Fore.WHITE}Enter new price: {Fore.YELLOW}"))
        try:
            new_price = float(new_price)
        except (ValueError, TypeError):
            print(f"{Fore.RED}Oops :-( Invalid Input!")
            sleep(1)
            continue
        if new_price < 0:
            print(f"{Fore.RED}Invalid input! Price must be more than 0!")
            continue
        if new_price > 0:
            parking.set_price_per_day(new_price)
            print(f"{Fore.WHITE}The price set to {Fore.GREEN}{new_price}")
            break

def set_price_per_hour():
    while True:
        print(Fore.LIGHTBLACK_EX + "Current price per hour: ", parking.get_price_per_hour())
        new_price = input((f"{Fore.WHITE}Enter new price: {Fore.YELLOW}"))
        try:
            new_price = float(new_price)
        except (ValueError, TypeError):
            print(f"{Fore.RED}Oops :-( Invalid Input!")
            sleep(1)
            continue
        if new_price < 0:
            print(f"{Fore.RED}Invalid input! Price must be more than 0!")
            continue
        if new_price > 0:
            parking.set_price_per_hour(new_price)
            print(f"{Fore.WHITE}The price set to {Fore.GREEN}{new_price}")
            break

def set_maximum_capacity():
    while True:
        print(Fore.LIGHTBLACK_EX + "Current price per hour: ", parking.get_maximum_capacity())
        new_camp = input((f"{Fore.WHITE}Enter new campacity: {Fore.YELLOW}"))
        try:
            new_camp = int(new_camp)
        except (ValueError, TypeError):
            print(f"{Fore.RED}Oops :-( Invalid Input!")
            sleep(1)
            continue
        if new_camp < 0:
            print(f"{Fore.RED}Invalid input! Price must be more than 0!")
            continue
        if new_camp > 0:
            parking.set_maximum_capacity(new_camp)
            print(f"{Fore.WHITE}The campacity set to {Fore.GREEN}{new_camp}")
            break

# To edit
def calculate_price():
    car_number = input(f"Enter a License number: {Fore.YELLOW}")
    print(f'{Fore.WHITE}Price: {Fore.RED}{parking.calculate_price(car_number)} $')

def exit():
    sleep(1)
    while True:
        try:
            fin = int(input(f"""
            {Fore.WHITE}1. {Fore.GREEN}Back to menu 
            {Fore.WHITE}2. {Fore.RED}Quit 
            {Fore.WHITE}"""))
        except (ValueError, TypeError):
            continue
        if fin not in (1, 2):
            print(Fore.RED + f"Invalid Input! Please Enter a Valid Option From The Menu!")
            continue
        if fin == 1:
            break
        if fin == 2:
            save_parking()
            print(Fore.WHITE + f"Logging out...")
            sleep(0.5)
            sys.exit(0)

####################################################################################
######################################  MENU  ######################################
####################################################################################

#Never touch tihs!
db = 'parking_data.db'
if os.path.exists(db):
    with open(db, 'rb') as file:
        parking = pickle.load(file)
else:
    parking = ParkingLot()


entry_menu = (
    f"""{Fore.GREEN}Welcome to my parking lot!"""
)

user_select_menu = (
    f"""{Fore.LIGHTBLUE_EX}Please choose an option:
        {Fore.WHITE}1. Enter as Admin
        {Fore.WHITE}2. Enter as User
        {Fore.WHITE}3. Exit
    """
)

admin_console = (
    f"""{Fore.GREEN}Welcome to the admin console!
        {Fore.WHITE}Please choose an option:
        {Fore.WHITE}1. Set parking price per hour
        {Fore.WHITE}2. Set parking price per day
        {Fore.WHITE}3. Set parking lot campacity
        {Fore.WHITE}4. Reset parking lot
        
        {Fore.WHITE}5. Back to main menu
        {Fore.WHITE}6. Quit
    """
)

user_console = (
    f"""{Fore.GREEN}Welcome to the user console!
        {Fore.WHITE}Please choose an option:
        {Fore.WHITE}1. Enter car
        {Fore.WHITE}2. Exit car
        {Fore.WHITE}3. Cars in lot report
        {Fore.WHITE}4. Car in lot over 24 hours report
        {Fore.WHITE}5. Check toll fee for a vehicle

        {Fore.WHITE}6. Back to main menu
        {Fore.WHITE}7. Quit
    """
)

####################################################################################
######################################  MAIN  ######################################
####################################################################################

while True:
    try:
        print(entry_menu)
        print(Fore.LIGHTBLACK_EX + "Price per hour: ", parking.get_price_per_hour())
        print(Fore.LIGHTBLACK_EX + "Price per day: ", parking.get_price_per_day())
        print(Fore.LIGHTBLACK_EX + "Avalble parking space: ", parking.avalble_space_in_lot()) 
        user_input = int(input(f"\n{user_select_menu}\n"))
    except (ValueError, TypeError):
        print(Fore.RED + f"Invalid Input! Please Enter a Valid Option From The Menu!")
        sleep(1.5)
        continue
    if user_input not in [1, 2, 3]:
        print(Fore.RED + f"Invalid Input! Please Enter a Valid Option From The Menu!")
        sleep(1.5)
        continue
    if user_input == 3:
        save_parking()
        print("Logging out...")
        sleep(1.5)
        sys.exit(0)
    if user_input == 2:
        ## User Console
        while True:
            print(user_console)
            try:
                user_console_input = int(input(""))
            except (ValueError, TypeError):
                print(Fore.RED + f"Oops :-( Invalid Input!")
                continue
            if user_console_input not in [1, 2, 3, 4, 5, 6, 7]:
                print(Fore.RED + f"Invalid Input! Please Enter a Valid Option From The Menu!")
                sleep(1.5)
                continue
            if user_console_input == 7:
                save_parking()
                print("Logging out...")
                sleep(1.5)
                sys.exit(0)
            if user_console_input == 6:
                break
            if user_console_input == 5:
                calculate_price()
                exit()
            if user_console_input == 4:
                parking.print_cars_above_24_hours()
                exit()
            if user_console_input == 3:
                parking.print_cars_in_lot()
                exit()
            if user_console_input == 2:
                get_car_to_remove()
                exit()
            if user_console_input == 1:
                get_car_details_from_user()
                exit()
    
    ## Admin Console 
    if user_input == 1:
        if password_policy():
            while True:
                print(admin_console)
                try:
                    admin_console_input = int(input(""))
                except (ValueError, TypeError):
                    print(Fore.RED + f"Oops :-( Invalid Input!")
                    continue
                if admin_console_input not in [1, 2, 3, 4, 5, 6]:
                    print(Fore.RED + f"Invalid Input! Please Enter a Valid Option From The Menu!")
                    sleep(1.5)
                    continue
                if admin_console_input == 6:
                    save_parking()
                    print("Logging out...")
                    sleep(1.5)
                    sys.exit(0)
                if admin_console_input == 5:
                    break
                if admin_console_input == 4:
                    parking.reset_lot()
                    exit()
                if admin_console_input == 3:
                    set_maximum_capacity()
                    exit()
                if admin_console_input == 2:
                    set_price_per_day()
                    exit()
                if admin_console_input == 1:
                    set_price_per_hour()
                    exit()
