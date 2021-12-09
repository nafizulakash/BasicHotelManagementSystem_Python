                       # Project Name-  Hotel Management System

import random

name = []
phoneNumber = []
add = []
room = []                                # [Blank Lists]
price = []
rc = []
p = []
roomNumber = []
customerId = []
day = []
i = 0


def home():
    print("\t\t\t\t\t\t Welcome to Hotel ABC\n")         # Welcome Note
    print("\t\t\t 1 Rooms Information & Booking\n")
    print("\t\t\t 2 Room Service(Menu Card)\n")          # Main menu
    print("\t\t\t 3 Payment\n")
    print("\t\t\t 4 Record\n")
    print("\t\t\t 0 Exit\n")

    ch = int(input("->"))                                # Choose a service

    if ch == 1:
        print(" ")
        booking()
    elif ch == 2:
        print(" ")
        restaurant()
    elif ch == 3:         # Using conditional statement based on user's choice which service he/she wants.
        print(" ")
        payment()
    elif ch == 4:
        print(" ")
        record()
    else:
        exit()


def booking():
    global i, totalDays                              # Declaring global variables.
    print(" BOOKING ROOMS")
    print(" ")

    while 1:
        n = str(input("Name: "))
        p1 = str(input("Phone No.: "))       # Collecting user's details like name, phone number and address.
        a = str(input("Address: "))
        totalDays = int(input("For How Many Days: "))
        if n != "" and p1 != "" and a != "":
            name.append(n)                   # Appending name into a list.
            add.append(a)
            break
        else:
            print("\tName, Phone no. & Address cannot be empty..!!")   # Printing user's details.

    print("----------Select Room----------")
    print(" 1. Standard Non-AC - 4000 BDT")
    print(" 2. Standard AC - 6000 BDT")             # 4 different types of room options.
    print(" 3. 3-Bed Non-AC - 12000 BDT")
    print(" 4. 3-Bed AC - 14000 BDT")

    ch = int(input("->"))     # Choose a room.

    if ch == 1:
        room.append('Standard Non-AC')
        print("Room Type - Standard Non-AC")
        price.append(4000)
        print("Price- 4000 BDT")
    elif ch == 2:
        room.append('Standard AC')
        print("Room Type - Standard AC")
        price.append(6000)
        print("Price- 6000 BDT")
    elif ch == 3:
        room.append('3-Bed Non-AC')
        print("Room Type - 3-Bed Non-AC")            # Using list to keep a record of user's room choice
        price.append(12000)
        print("Price- 12000 BDT")
    elif ch == 4:
        room.append('3-Bed AC')
        print("Room Type- 3-Bed AC")
        price.append(14000)
        print("Price- 14000 BDT")
    else:
        print(" Wrong choice!")

    rn = random.randrange(40) + 300     # Using random function
    cid = random.randrange(40) + 10

    while rn in roomNumber or cid in customerId:    # Creating a random customer id
        rn = random.randrange(60) + 300
        cid = random.randrange(60) + 10

    rc.append(0)
    p.append(0)

    if p1 not in phoneNumber:
        phoneNumber.append(p1)
    elif p1 in phoneNumber:
        for n in range(0, i):
            if p1 == phoneNumber[n]:
                if p[n] == 1:
                    phoneNumber.append(p1)
    elif p1 in phoneNumber:
        for n in range(0, i):
            if p1 == phoneNumber[n]:
                if p[n] == 0:
                    print("\tPhone no. already exists and payment yet not done..!!")
                    name.pop(i)
                    add.pop(i)
                    booking()
    print("")
    print("\t\t\t***ROOM BOOKED SUCCESSFULLY***\n")     # Room booking confirmation
    print("Room No. - ", rn)                            # Booked room number
    print("Customer Id - ", cid)                        # Customer id.
    roomNumber.append(rn)
    customerId.append(cid)
    i = i + 1
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()


def restaurant():                          # Food menu
    ph = int(input("Customer Id: "))
    global i
    f = 0
    r = 0
    for n in range(0, i):
        if customerId[n] == ph and p[n] == 0:
            f = 1
            print("-------------------------------------------------------------------------")
            print("                    Hotel ABC                                          ")
            print("-------------------------------------------------------------------------")
            print("                    Service Card                                       ")
            print("-------------------------------------------------------------------------")
            print("\n                        Foods                          ")
            print("---------------------------------------------------------")
            print(" 1 Tea......................................... 20.00 BDT")
            print(" 2 Coffee...................................... 50.00 BDT")
            print(" 3 Cold Drink.................................. 50.00 BDT")
            print(" 4 Breakfast Set Menu ........................ 150.00 BDT")                      # Service Menu
            print(" 5 Lunch/Dinner Set Menu ..................... 250.00 BDT")
            print(" 6 Ice-cream................................... 60.00 BDT")

            print("----------------------------------------------")
            print("----------------------------------------------")

            print("                         Recreations                     ")
            print("            ------------------------------------         ")
            print(" 7 Massage................................... 2000.00 BDT")
            print(" 8 Capella Musician (For 1.5 Hours).......... 4000.00 BDT")
            print("                             ")
            print("Press 0 -to end ")
            ch = 1
            while ch != 0:
                ch = int(input(" -> "))
                if ch == 1:
                    serviceCost = 20
                    r = r + serviceCost
                elif ch == 2 or ch == 3:
                    serviceCost = 50
                    r = r + serviceCost
                elif ch == 4:
                    serviceCost = 150
                    r = r + serviceCost
                elif ch == 5:
                    serviceCost = 250
                    r = r + serviceCost
                elif ch == 6:                           # Storing prices into 'r'
                    serviceCost = 60
                    r = r + serviceCost
                elif ch == 7:
                    serviceCost = 2000
                    r = r + serviceCost
                elif ch == 8:
                    serviceCost = 4000
                    r = r + serviceCost
                elif ch == 0:
                    pass
                else:
                    print("Wrong Choice..!!")
            print("Total Bill: ", r)
            r = r + rc.pop(n)
            rc.append(r)
        else:
            pass
    if f == 0:
        print("Invalid Customer Id")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()


def payment():
    ph = str(input("Phone Number: "))
    global i
    f = 0

    for n in range(0, i):
        if ph == phoneNumber[n]:
            if p[n] == 0:
                f = 1
                print(" Payment")
                print(" --------------------------------")
                print(" MODE OF PAYMENT")

                print(" 1- Credit/Debit Card")
                print(" 2- Cash")                           # 2 types of payment methods
                x = int(input("-> "))
                print("\n Amount: ", (price[n] * totalDays) + rc[n])            # Total Amount Calculations
                print("\n Pay For ABC")
                print(" (y/n)")                                 # If the user wants to pay the bill or not
                ch = str(input("->"))

                if ch == 'y' or ch == 'Y':
                    print("\n\n --------------------------------")
                    print("        Hotel ABC")
                    print(" --------------------------------")
                    print("           Bill")
                    print(" --------------------------------")
                    print(" Name: ", name[n], "\t\n Phone No.: ", phoneNumber[n], "\t\n Address: ", add[n], "\t")
                    print("\n Room Type: ", room[n], "\t\n Room Charges: ", price[n] * totalDays, "\t")         # Details of record
                    print(" Restaurant Charges: \t", rc[n])
                    print(" --------------------------------")
                    print("\n Total Amount: ", (price[n] * totalDays) + rc[n], "\t")
                    print(" --------------------------------")
                    print("        Thank You")
                    print("        Visit Again :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n, 1)

                    # pops room no. and customer id from list and
                    # later assigns zero at same position
                    roomNumber.pop(n)
                    customerId.pop(n)
                    roomNumber.insert(n, 0)
                    customerId.insert(n, 0)

            else:
                for j in range(n + 1, i):
                    if ph == phoneNumber[j]:
                        if p[j] == 0:
                            pass

                        else:
                            f = 1
                            print("\n\tPayment has been Made :)\n\n")
    if f == 0:
        print("Invalid Customer Id")

    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()


def record():
    if phoneNumber:
        print("     *** HOTEL RECORD ***\n")
        print("| Name   | Phone No. | Address | Room Type  | Price    |")
        print("-----")
        for n in range(0, i):
            print("|", name[n], "\t |", phoneNumber[n], "\t|", add[n], room[n], "\t|", price[n])            # Details of record
        print("-----")
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        home()
    else:
        exit()


home()

