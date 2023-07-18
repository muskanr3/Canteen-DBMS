import subprocess as sp
import pymysql
import pymysql.cursors
from tabulate import tabulate

# choice 1
def selection():
    while 1:
        try:
            print(
                "1. Display all the food items available at a particular price (as specified by the user)."
            )
            print("2. Display all the details of the staff working in a certain canteen. ")
            chSelect = int(input("Enter choice: "))

            if chSelect == 1:
                price = float(
                    input("Enter the price at which food items should be displayed: ")
                )
                query = "select Food_Name as Food from Food where Price = {}".format(price)

            elif chSelect == 2:
                cname = input("Enter canteen name: ")
                query = "select SD.Aadhar_Number, SD.Fname, SD.Mname , SD.Lname, SD.Age, SD.Gender from Staff_Details SD, Staff S where S.Aadhar_Number = SD.Aadhar_Number and S.Canteen_Name = '{}'".format(
                    cname
                )

            else:
                print("Invalid Input!")
                return
            mycur.execute(query)
            output = mycur.fetchall()

            if mycur.rowcount != 0:
                print()
                print("Output: ")
                print(tabulate(output, headers="keys", tablefmt="grid"))
            else:
                print()
                print("No rows selected")
        except Exception as e:
            mycon.rollback()
            print("Failed to insert record into database")
            print(">>>>>>>>>>>>>", e)

        return

# choice 2
def projection():
    while 1:
        try:
            print()
            print("1. To display the names of all the beverages that have a price more than Rs 35.")
            print("2. To display the details of the customers who are older than 19.")
            print()
            chProj = int(input("Enter choice: "))

            if chProj == 1:
                query = "select Beverage_Name from Beverages where Price > 35"

            elif chProj == 2:
                query = "select C.Aadhar_Number,C.Name,C.Date_of_Birth,Cp.Phone_Number from Customer C ,Customer_Ph_Number Cp where C.Aadhar_Number = Cp.Cust_Aadhar and year(curdate()) - year(C.Date_of_Birth) > 19"
            
            else:
                print()
                print("Invalid Input!")
                return
            mycur.execute(query)
            output = mycur.fetchall()
            if mycur.rowcount != 0:
                print()
                print("Output: ")
                print(tabulate(output , headers = "keys" , tablefmt = "grid"))
            else:
                print()
                print("No rows selected!")

        except Exception as e:
            mycon.rollback()
            print("Failed to insert record into database")
            print(">>>>>>>>>>>>>", e)
        return


def HireMessCommitteeMember():
    """
    This is to add a new mess committee member to the mess committee table.
    """
    try:
        # Takes employee details as input
        row = {}
        print()
        print("Enter new mess committee member's details: ")
        row["M_ID"] = int(input("Enter Member ID: "))
        row["Member_Name"] = input("Enter Member Name: ")
        row["Age"] = int(input("Enter Member Age: "))
        row["Designation"] = input("Enter Member Designation: ")

        query = (
            "INSERT INTO Mess_Committee(M_ID, Member_Name, Age, Designation) VALUES('%d', '%s', '%d', '%s')"
            % (
                row["M_ID"],
                row["Member_Name"],
                row["Age"],
                row["Designation"],
            )
        )

        mycur.execute(query)
        mycon.commit()

        print("Inserted Record Into Database")

    except Exception as e:
        mycon.rollback()
        print("Failed to insert record into database")
        print(">>>>>>>>>>>>>", e)

    return

def insertCanteen():
    """
    This is to add a new canteen to the canteen table.
    """
    try:
        # Takes canteen details as input
        print()
        row = {}
        print("Enter new canteen details: ")
        row["Canteen_Name"] = input("Enter Canteen Name: ")
        row["Location"] = input("Enter Location: ")
        row["Year_of_Opening"] = int(input("Enter Year of Opening (YYYY-MM-DD): "))
        row["Opening_Time"] = input("Enter Opening Time (HH:MM): ")
        row["Closing_Time"] = input("Enter Closing Time (HH:MM): ")
        row["Mess_Manager_ID"] = int(input("Enter Mess Manager ID: "))
        
        query = (
            "INSERT INTO Canteen(Canteen_Name, Location, Year_of_Opening, Opening_Time, Closing_Time, Mess_Manager_ID) VALUES('%s', '%s', '%d', '%s', '%s', '%d')"
            % (
                row["Canteen_Name"],
                row["Location"],
                row["Year_of_Opening"],
                row["Opening_Time"],
                row["Closing_Time"],
                row["Mess_Manager_ID"],

            )
        )

        print(query)
        mycur.execute(query)
        mycon.commit()

        print("Inserted Record Into Database")

    except Exception as e:
        mycon.rollback()
        print("Failed to insert record into database")
        print(">>>>>>>>>>>>>", e)

    return

# choice 5
def insert():
    # insert a mess committee member or new canteen
    print()
    print("1. Insert a mess committee member: ")
    print("2. Insert a new Canteen: ")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        HireMessCommitteeMember()
    elif choice==2:
        insertCanteen()
    else:   
        print()
        print("invalid input")
    return 0

# choice 6


def bevUpdate():
    try:
        print()
        print("Enter beverage and its new price: ")
        bev = input("Enter beverage: ")
        newPrice = int(input("Enter new price: "))

        query = "UPDATE Beverages SET Price = %d where Beverage_Name = '%s'" % (
            newPrice,
            bev,
        )

        print(query)
        mycur.execute(query)
        mycon.commit()

        print("Query executed.")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute query.")
        print(">>>>>>>>>>>>>", e)

    return


def dependentsUpdate():
    try:
        print()
        row = {}
        print("Enter dependent and his/her new Staff: ")
        dep = input("Enter dependent: ")
        newStaff = int(input("Enter new S_ID of the staff: "))

        query = "UPDATE Dependent SET S_ID = %d where Dependent_Name = '%s'" % (
            newStaff,
            dep,
        )

        print(query)
        mycur.execute(query)
        mycon.commit()

        print("Query executed.")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute query.")
        print(">>>>>>>>>>>>>", e)

    return

def update():
    while 1:
        # update the cost of beverages
        print()
        print("1. Update the cost of a beverage: ")
        # update the dependentsname of a staff member
        print("2. Update the dependents of a staff member: ")
        choice = int(input("Enter update choice: "))
        if choice == 1:
            bevUpdate()
        elif choice == 2:
            dependentsUpdate()
        else:
            print("Invalid input")
        return

def AvgCost():
    try:
        query = "SELECT AVG(Price) AS Average_Cost FROM Beverages;"
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return


def MinSalary():
    try:
        query = "SELECT MIN(Salary) AS Minimum_Salary FROM Staff;"
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def aggregate():
    while 1:
        print("1. Display AVG cost of a beverage in a canteen.")
        print("2. Display MIN salary paid to the staff working in the canteen.")

        option = int(input("Enter choice: "))

        if option == 1:
            AvgCost()
        elif option == 2:
            MinSalary()
        else:
            print("Invalid Input")
        return

def SearchInventory():
    try:
        query = "SELECT Canteen_Name, Item_Name, Total_Quantity_Ordered - Quantity_Utilised \
                    AS Quantity_Remaining \
                    FROM Inventory;"
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def SearchCustomer():
    try:
        query = "SELECT Name FROM Customer WHERE Name LIKE 'T%';"
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def SearchCompany():
    try:
        length = int(input("Enter required length for Company Name: "))
        query = ("SELECT Name FROM Company WHERE CHAR_LENGTH(Name) = %d;" %(length))
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def search():
    while 1:
        print()
        print("1. Search for the items in the inventory by the item name and check the quantity remaining")
        print("2. Search for the customers with names that start with the letter T.")
        print("3. Search for Company names of length x letters.")

        print()
        option = int(input("Enter choice: "))

        if option == 1:
            SearchInventory()
        elif option == 2:
            SearchCustomer()
        elif option == 3:
            SearchCompany()
        else:
            print("Invalid Input")
        return

def PopularFood():
    try:
        query = "SELECT Food_Name, COUNT(*) \
                    AS No_of_Orders \
                    FROM Serves \
                    GROUP BY Food_Name \
                    ORDER BY COUNT(*) \
                    DESC LIMIT 1;"
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def OrderItem():
    try:
        print()
        item_order = int(input("Enter threshold value for ordering: "))
        query = ("SELECT Canteen_Name, Item_Name \
                    FROM Inventory \
                    WHERE Total_Quantity_Ordered - Quantity_Utilised <= %d;" %(item_order))
        mycur.execute(query)
        output = mycur.fetchall()
        if mycur.rowcount != 0:
            print()
            print("Output: ")
            print(tabulate(output , headers = "keys" , tablefmt = "grid"))
        else:
            print()
            print("No rows selected!")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def analysis():
    while 1:
        print()
        print("1. Analyse the quantity of an item remaining in order to determine when to place an order to a company.")
        print("2. Determine the most popular item from each canteen so canteens can place orders in a more cost efficient manner.")

        option = int(input("Enter choice: "))

        if option == 1:
            OrderItem()
        elif option == 2:
            PopularFood()
        else:
            print("Invalid Input")
        return


def DeleteStaff():
    try:
        print()
        Aadhar = int(input("Enter the Aadhar of the Staff Member: "))
        query = ("DELETE FROM Staff_Details WHERE Aadhar_Number = %d" %(Aadhar))
        mycur.execute(query)
        # print(mycur.fetchall())
        mycon.commit()
        print("Query executed.")

    except Exception as e:
        mycon.rollback()
        print("Failed to execute")
        print(">>>>>>>>>>>>>", e)

    return

def delete():
    print()
    print("1. Delete the record of staff not working in a canteen anymore.")
    DeleteStaff()
    return
        

def mapFuncCall(ch):
    """
    This function maps the choice entered by the user to the correct function.
    """
    if ch == 1:
        selection()
    elif ch == 2:
        projection()
    elif ch == 3:
        aggregate()
    elif ch == 4:
        search()
    elif ch == 5:
        insert()
    elif ch == 6:
        update()
    elif ch == 7:
        delete()
    elif ch == 8:
        analysis()

# Global
while 1:
    tmp = sp.call("clear", shell=True)

    username = input("Username: ")
    password = input("Password: ")

    try:
        mycon = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="Maanasa@4mysql",
            db="Final",
            cursorclass=pymysql.cursors.DictCursor,
        )

        tmp = sp.call("clear", shell=True)

        if mycon.open:
            print("Connected to database!")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE >")

        mycur = mycon.cursor()

        while 1:
            tmp = sp.call("clear", shell=True)

            # Note: PLS CHANGE THE MENU (I AM JUST GIVING THE BASIC FORMAL OPTIONS FOR NOW)
            print()
            print("1. Press 1 for SELECTION")
            print("2. Press 2 for PROJECTION")
            print("3. Press 3 for AGGREGATE")
            print("4. Press 4 for SEARCH")
            print("5. Press 5 for INSERT")
            print("6. Press 6 for UPDATE")
            print("7. Press 7 for DELETE")
            print("8. Press 8 for ANALYSIS")
            print("9. Logout")
            print()
            ch = int(input("Enter choice: "))
            tmp = sp.call("clear", shell=True)
            if ch == 9:
                exit()
            else:
                mapFuncCall(ch)
                tmp = input("Enter any key to CONTINUE > ")

    except Exception as e:
        tmp = sp.call("clear", shell=True)
        print(e)
        print(
            "Connection Refused: Either username or password is incorrect or user doesn't have access to database"
        )
        tmp = input("Enter any key to CONTINUE > ")
