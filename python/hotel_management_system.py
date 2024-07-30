import random
import datetime

name = []
address = []
phone_no = []
checkin_dates = []
checkout_dates = []
booking_Duration = []
custid = []
roomno = []
room = []
price = []
p = []


# global variable declaration

i = 0

# Home function
def Home():
    
    print("\t\t  =========== WELCOME TO HOTEL DARBAR ===========\n")
    print("\t\t\t 1 Booking\n")
    print("\t\t\t 2 Rooms Info\n")
    print("\t\t\t 3 Room Service (Menu Card)\n")
    print("\t\t\t 4 payment\n")
    print("\t\t\t 5 Record\n")
    print("\t\t\t 0 Exit")
    print("\t\t","="*50)

    ch = int(input("-->"))

    if (ch==1):
        print(" ")
        Booking()
    
    elif(ch==2):
        print(" ")
        Rooms_info()

    elif(ch==3):
        print(" ")
        restaurant()

    elif(ch==4):
        print(" ")
        Payment()

    elif(ch==5):
        print(" ")
        Record()

    else:
        exit()

# Function used in bookings


# booking function
def Booking():
    print("BOOKING ROOMS")
    print(" ")

    while True:
        n = str(input("Name : "))
        p1 = int(input("phone No. : "))
        a = str(input("Address : "))
        
        # check if any field is not empty
        if n and p1 and a :
            break
        else:
            print("\tName. Phone no. & Address cannot be empty..!!")
        
    checkin_date = input("Check-In (YYYY/MM/DD): ")
    checkout_date = input("Check-Out (YYYY/MM/DD): ")

    try:
        checkin = datetime.datetime.strptime(checkin_date, "%Y/%m/%d")
        checkout = datetime.datetime.strptime(checkout_date, "%Y/%m/%d")

        if checkout <= checkin:
            print("\nErr..!!\nCheck-Out date must be after Check-In\n")
            return Booking()
        
        duration = (checkout - checkin).days

        # storing information
        name.append(n)
        phone_no.append(p1)
        address.append(a)
        checkin_dates.append(checkin_date)
        checkout_dates.append(checkout_date)
        booking_Duration.append(duration)
    
    except ValueError:
        print("\nErr..!!\nInvalid date format. Please use YYYY/MM/DD\n")
        return Booking()
    
    select_room_type()
    
def select_room_type():
    print("----SELECT ROOM TYPE----")
    print(" 1. Standard Non-AC")
    print(" 2. Standard AC")
    print(" 3. 3-Bed Non-AC")
    print(" 4. 3-Bed AC")
    print("\t\tPress 0 for Room Prices")

    choice = int(input("->"))

    if choice == 0:
        display_room_prices()
    elif choice == 1:
        book_room('Standard Non-AC', 3500)
    elif choice == 2:
        book_room('Standard AC', 4000)
    elif choice == 3:
        book_room('3-Bed Non-AC', 4500)
    elif choice == 4:
        book_room('3-Bed AC', 5000)
    else:
        print("Wrong choice..!!")


def display_room_prices():
    print(" 1. Standard Non-AC - Rs. 3500")
    print(" 2. Standard AC - Rs. 4000")
    print(" 3. 3-Bed Non-AC - Rs. 4500")
    print(" 4. 3-Bed AC - Rs. 5000")
    choice = int(input("->"))
    if choice >= 1 and choice <= 4:
        room_types = ['Standard Non-AC', 'Standard AC', '3-Bed Non-AC', '3-Bed AC']
        room_prices = [3500, 4000, 4500, 5000]
        book_room(room_types[choice - 1], room_prices[choice - 1])
    else:
        print("Wrong choice..!!")


def book_room(room_type, room_price):
    room.append(room_type)
    print(f"Room Type - {room_type}")
    price.append(room_price)
    print(f"Price - {room_price}")

    # Generate room number and customer id
    rn, cid = generate_room_and_customer_id()

    roomno.append(rn)
    custid.append(cid)

    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***")
    print(f"Room No. - {rn}")
    print(f"Customer Id - {cid}")

    global i
    i += 1

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()


def generate_room_and_customer_id():
    rn = random.randrange(40) + 300
    cid = random.randrange(40) + 10

    # Ensure the generated room number and customer id are not already allocated
    while rn in roomno or cid in custid:
        rn = random.randrange(60) + 300
        cid = random.randrange(60) + 10

    return rn, cid


# Rooms_info function
def Rooms_info():
    print("\nSTANDARD NON-AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofas, Balcony, and")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("3-Bed NON-AC")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofas, 1")
    print("an attached washroom with hot/cold water + Window/Split AC.\n")
    print("Side table, Balcony with an Accent table with 2 chairs, and an")
    print("Double-Door Cupboard, 1 Coffee table with 2 sofas, Balcony, and")
    print("attached washroom with hot/cold water.\n")
    print("3-Bed AC")
    print("---------------------------------------------------------------")
    print("Room amenities include: 1 Double Bed, Television, Telephone,")
    print("Room amenities include: 1 Double Bed + 1 Single Bed, Television,")
    print("---------------------------------------------------------------")
    print("Telephone, a Triple-Door Cupboard, 1 Coffee table with 2 sofas,")
    print("STANDARD AC")
    print("1 Side table, Balcony with an Accent table with 2 chairs, and an")
    print("an attached washroom with hot/cold water.\n")
    print("attached washroom with hot/cold water + Window/Split AC.\n\n")
    print(" ------ HOTEL ROOMS INFO ------")

    ch = int(input("Enter choice : \n0 for back\n-->"))
    if ch == 0:
        Home()
    else:
        exit()


def display_menu():
    print("-------------------------------------------------------------------------")
    print("                   Hotel AnCasa")
    print("-------------------------------------------------------------------------")
    print("                   Menu Card")
    print("-------------------------------------------------------------------------")
    print("\n BEVERAGES                               26 Dal Fry................ ₹140.00")
    print("----------------------------------     27 Dal Makhani............ ₹150.00")
    print(" 1 Regular Tea............. ₹20.00     28 Dal Tadka.............. ₹150.00")
    print(" 2 Masala Tea.............. ₹25.00")
    print(" 3 Coffee.................. ₹25.00     ROTI")
    print(" 4 Cold Drink.............. ₹25.00     ----------------------------------")
    print(" 5 Bread Butter............ ₹30.00     29 Plain Roti.............. ₹15.00")
    print(" 6 Bread Jam............... ₹30.00     30 Butter Roti............. ₹15.00")
    print(" 7 Veg. Sandwich........... ₹50.00     31 Tandoori Roti........... ₹20.00")
    print(" 8 Veg. Toast Sandwich..... ₹50.00     32 Butter Naan............. ₹20.00")
    print(" 9 Cheese Toast Sandwich... ₹70.00")
    print(" 10 Grilled Sandwich........ ₹70.00     RICE")
    print("                                      ----------------------------------")
    print(" SOUPS                                 33 Plain Rice.............. ₹90.00")
    print("----------------------------------     34 Jeera Rice.............. ₹90.00")
    print(" 11 Tomato Soup............ ₹110.00     35 Veg Pulao.............. ₹110.00")
    print(" 12 Hot & Sour............. ₹110.00     36 Peas Pulao............. ₹110.00")
    print(" 13 Veg. Noodle Soup....... ₹110.00")
    print(" 14 Sweet Corn............. ₹110.00     SOUTH INDIAN")
    print(" 15 Veg. Munchow........... ₹110.00     ----------------------------------")
    print("                                      37 Plain Dosa............. ₹100.00")
    print(" MAIN COURSE                            38 Onion Dosa............. ₹110.00")
    print("----------------------------------     39 Masala Dosa............ ₹130.00")
    print(" 16 Shahi Paneer........... ₹110.00     40 Paneer Dosa............ ₹130.00")
    print(" 17 Kadai Paneer........... ₹110.00     41 Rice Idli.............. ₹130.00")
    print(" 18 Handi Paneer........... ₹120.00     42 Sambhar Vada........... ₹140.00")
    print(" 19 Palak Paneer........... ₹120.00")
    print(" 20 Chilli Paneer.......... ₹140.00     ICE CREAM")
    print(" 21 Matar Mushroom......... ₹140.00     ----------------------------------")
    print(" 22 Mix Veg................ ₹140.00     43 Vanilla................. ₹60.00")
    print(" 23 Jeera Aloo............. ₹140.00     44 Strawberry.............. ₹60.00")
    print(" 24 Malai Kofta............ ₹140.00     45 Pineapple............... ₹60.00")
    print(" 25 Aloo Matar............. ₹140.00     46 Butter Scotch........... ₹60.00")
    print("Press 0 - to end")

def restaurant():
    customer_id = int(input("Customer ID: "))
    global i

    found_customer = False
    total_bill = 0

    for n in range(i):
        if n < len(custid) and custid[n] == customer_id and p[n] == 0:
            found_customer = True
            display_menu()
            choice = 1

            while choice != 0:
                choice = int(input(" -> "))

                # Prices for menu items
                menu_prices = {
                    1: 20.00, 2: 25.00, 3: 25.00, 4: 25.00, 5: 30.00,
                    6: 30.00, 7: 50.00, 8: 50.00, 9: 70.00, 10: 70.00,
                    11: 110.00, 12: 110.00, 13: 110.00, 14: 110.00, 15: 110.00,
                    16: 110.00, 17: 110.00, 18: 120.00, 19: 120.00, 20: 140.00,
                    21: 140.00, 22: 140.00, 23: 140.00, 24: 140.00, 25: 140.00,
                    26: 140.00, 27: 150.00, 28: 150.00, 29: 15.00, 30: 15.00,
                    31: 20.00, 32: 20.00, 33: 90.00, 34: 90.00, 35: 110.00,
                    36: 110.00, 37: 100.00, 38: 110.00, 39: 130.00, 40: 130.00,
                    41: 130.00, 42: 140.00, 43: 60.00, 44: 60.00, 45: 60.00, 46: 60.00
                }

                if choice in menu_prices:
                    item_price = menu_prices[choice]
                    total_bill += item_price
                elif choice == 0:
                    break
                else:
                    print("Wrong Choice..!!")

            print("Total Bill: ₹", total_bill)
            total_bill += rc[n]

    if not found_customer:
        print("Invalid Customer ID")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()


def Payment():
    pass

def Record():
    if not name:
        print("No Records Found .....")
    else:
        print("Records of hotel DARBAR")
        print("| Name\t| Phone No\t| Address\t| Check-IN\t | Check-OUT\t| Room Type\t| Price\t|")
        for n in range(i):
            print(f"| {name[n]}\t| {phone_no[n]}\t| {address[n]}\t| {checkin_dates[n]}\t| {checkout_dates[n]}\t| {room[n]}\t| {price[n]}|") 
    
    ch = int(input("Enter choice : \n0 for back\n-->"))
    if ch == 0:
        Home()
    else:
        exit()












# Driver code
Home()