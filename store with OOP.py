import os
import sqlite3


class Store:
    storeDB = dbCursor = None

    def __init__(self):
        global storeDB, dbCursor
        storeDB = sqlite3.connect('store.db')
        dbCursor = storeDB.cursor()

    def __del__(self):
        storeDB.commit()


class itemCreation(Store):
    def createTable(self, mode='DESC'):
        dbCursor.execute("""CREATE TABLE IF NOT EXISTS store (itemID, itemName, itemPrice)""")

    def insertItem(self):
        try:
            dbCursor.execute("INSERT INTO store values (1, 'Basketball Shoes', 90)")
            dbCursor.execute("INSERT INTO store values (2, 'Basketball Socks', 10)")
            dbCursor.execute("INSERT INTO store values (3, 'Basketball Jersey', 50)")
            dbCursor.execute("INSERT INTO store values (4, 'Hoodie', 70)")
            dbCursor.execute("INSERT INTO store values (5, 'Short', 30)")
        except Exception as e:
            return e


class customer(itemCreation):
    itemID = None

    def __init__(self):
        global itemID
        print("-----------------Welcome to Martin Lau Store--------------------")
        dbCursor.execute("SELECT * FROM store")
        display = dbCursor.fetchall()
        for row in display:
            print(f"#{str(row[0])} {row[1]} | Price: $" + "{:.2f}".format(row[2]))
        self.dashedLine()
        itemID = input("Which item would you like to buy? (Select 1 to 5 or type 6 to stop): ")

    def dashedLine(self):
        for i in range(0, 1):
            for j in range(0, i + 50):
                print("_", end="_")
        print(" ")

    def itemSelection(self):
        while True:
            self.__init__()
            if itemID == "1":
                # Selection of item1
                print(self.item1())
            elif itemID == "2":
                # Selection of item2
                print(self.item2())
            elif itemID == "3":
                # Selection of item3
                print(self.item3())
            elif itemID == "4":
                # Selection of item4
                print(self.item4())
            elif itemID == "5":
                # Selection of item5
                print(self.item5())
            elif "1" > itemID < "6":
                print("\n It must be between 1 and 6")
            elif itemID == "6":
                print("See you next time!")
                exit()

    def item1(self):
        dbCursor.execute("SELECT * FROM store WHERE itemID = 1")
        record = dbCursor.fetchall()
        # splits the variables into different sections
        for row in record:
            itemID = row[0]
            itemName = row[1]
            itemPrice = row[2]

        choice = input("Would you like to add this item to your selection? (yes or no else stop the program) ")
        if choice.lower() == "yes":
            name = input("Can I have your name? ")
            # checks if the customer exist in the database, else create a database for the customer
            if self.customerCheck(name):
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Inserts the item that the customer requested to add into the purchase cart
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)
            else:
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Creates the database for the customer and creates a table of receipt for him
                customerCur.execute("""CREATE TABLE IF NOT EXISTS receipt (itemID, itemName, itemPrice)""")
                # Adds the item into the customers cart in the database
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)

            # asks if the user wants to add more items
            anythingElse = input("Would you like to add anything else? (yes or no else stop the program) ")
            if anythingElse.lower() == "yes":
                self.itemSelection()
            else:
                print("Thank You for buying with us!")
                self.displayReceipt(name)
                exit()
        elif choice.lower() == "no":
            print("Make another selection")
            self.itemSelection()
        else:
            print("See You Around!")
            exit()

    def item2(self):
        dbCursor.execute("SELECT * FROM store WHERE itemID = 2")
        record = dbCursor.fetchall()
        # splits the variables into different sections
        for row in record:
            itemID = row[0]
            itemName = row[1]
            itemPrice = row[2]

        choice = input("Would you like to add this item to your selection? (yes or no else stop the program) ")
        if choice.lower() == "yes":
            name = input("Can I have your name? ")
            # checks if the customer exist in the database, else create a database for the customer
            if self.customerCheck(name):
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Inserts the item that the customer requested to add into the purchase cart
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)
            else:
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Creates the database for the customer and creates a table of receipt for him
                customerCur.execute("""CREATE TABLE IF NOT EXISTS receipt (itemID, itemName, itemPrice)""")
                # Adds the item into the customers cart in the database
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)

            # asks if the user wants to add more items
            anythingElse = input("Would you like to add anything else? (yes or no else stop the program) ")
            if anythingElse.lower() == "yes":
                self.itemSelection()
            else:
                print("Thank You for buying with us!")
                self.displayReceipt(name)
                exit()
        elif choice.lower() == "no":
            print("Make another selection")
            self.itemSelection()
        else:
            print("See You Around!")
            exit()

    def item3(self):
        dbCursor.execute("SELECT * FROM store WHERE itemID = 3")
        record = dbCursor.fetchall()
        # splits the variables into different sections
        for row in record:
            itemID = row[0]
            itemName = row[1]
            itemPrice = row[2]

        choice = input("Would you like to add this item to your selection? (yes or no else stop the program) ")
        if choice.lower() == "yes":
            name = input("Can I have your name? ")
            # checks if the customer exist in the database, else create a database for the customer
            if self.customerCheck(name):
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Inserts the item that the customer requested to add into the purchase cart
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)
            else:
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Creates the database for the customer and creates a table of receipt for him
                customerCur.execute("""CREATE TABLE IF NOT EXISTS receipt (itemID, itemName, itemPrice)""")
                # Adds the item into the customers cart in the database
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)

            # asks if the user wants to add more items
            anythingElse = input("Would you like to add anything else? (yes or no else stop the program) ")
            if anythingElse.lower() == "yes":
                self.itemSelection()
            else:
                print("Thank You for buying with us!")
                self.displayReceipt(name)
                exit()
        elif choice.lower() == "no":
            print("Make another selection")
            self.itemSelection()
        else:
            print("See You Around!")
            exit()

    def item4(self):
        dbCursor.execute("SELECT * FROM store WHERE itemID = 4")
        record = dbCursor.fetchall()
        # splits the variables into different sections
        for row in record:
            itemID = row[0]
            itemName = row[1]
            itemPrice = row[2]

        choice = input("Would you like to add this item to your selection? (yes or no else stop the program) ")
        if choice.lower() == "yes":
            name = input("Can I have your name? ")
            # checks if the customer exist in the database, else create a database for the customer
            if self.customerCheck(name):
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Inserts the item that the customer requested to add into the purchase cart
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)
            else:
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Creates the database for the customer and creates a table of receipt for him
                customerCur.execute("""CREATE TABLE IF NOT EXISTS receipt (itemID, itemName, itemPrice)""")
                # Adds the item into the customers cart in the database
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)

            # asks if the user wants to add more items
            anythingElse = input("Would you like to add anything else? (yes or no else stop the program) ")
            if anythingElse.lower() == "yes":
                self.itemSelection()
            else:
                print("Thank You for buying with us!")
                self.displayReceipt(name)
                exit()
        elif choice.lower() == "no":
            print("Make another selection")
            self.itemSelection()
        else:
            print("See You Around!")
            exit()

    def item5(self):
        dbCursor.execute("SELECT * FROM store WHERE itemID = 5")
        record = dbCursor.fetchall()
        # splits the variables into different sections
        for row in record:
            itemID = row[0]
            itemName = row[1]
            itemPrice = row[2]

        choice = input("Would you like to add this item to your selection? (yes or no else stop the program) ")
        if choice.lower() == "yes":
            name = input("Can I have your name? ")
            # checks if the customer exist in the database, else create a database for the customer
            if self.customerCheck(name):
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Inserts the item that the customer requested to add into the purchase cart
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)
            else:
                customerDatabase = sqlite3.connect(name + '.db')
                customerCur = customerDatabase.cursor()
                # Creates the database for the customer and creates a table of receipt for him
                customerCur.execute("""CREATE TABLE IF NOT EXISTS receipt (itemID, itemName, itemPrice)""")
                # Adds the item into the customers cart in the database
                customerCur.execute("INSERT INTO receipt VALUES (?, ?, ?);", (itemID, itemName, itemPrice))
                customerDatabase.commit()
                customerDatabase.close()
                self.displayReceipt(name)

            # asks if the user wants to add more items
            anythingElse = input("Would you like to add anything else? (yes or no else stop the program) ")
            if anythingElse.lower() == "yes":
                self.itemSelection()
            else:
                print("Thank You for buying with us!")
                self.displayReceipt(name)
                exit()
        elif choice.lower() == "no":
            print("Make another selection")
            self.itemSelection()
        else:
            print("See You Around!")
            exit()

    def customerCheck(self, name):
        if os.path.isfile(name + '.db'):
            return True
        else:
            return False

    def displayReceipt(self, customerName):
        totalPrice = 0
        print("-----------Receipt-----------")
        customerInfo = sqlite3.connect(customerName + ".db")
        customerCur = customerInfo.cursor()
        customerCur.execute("SELECT * FROM receipt")
        # records all the customers cart into one list
        records = customerCur.fetchall()
        customerCur.execute("SELECT * FROM receipt GROUP BY itemID HAVING COUNT(*)  = 1;")
        # records all the different items found in the customers cart
        differentItems = customerCur.fetchall()
        customerCur.execute("SELECT * FROM receipt GROUP BY itemID HAVING COUNT(*)  > 1;")
        # records all the duplicate items found in the customers cart
        duplicates = customerCur.fetchall()

        # It add the differentItems price together
        for i in differentItems:
            totalPrice += i[2]

        # It displays the records of all items and their prices
        for i in records:
            print("#" + str(i[0]) + " " + i[1] + " | Price: $" + "{:.2f}".format(i[2]))

        # It adds the duplicateItem prices together and puts a discount on them
        for i in duplicates:
            print("-------------You have 50% discount in this item " + i[1] + "---------------")
            totalPrice += i[2] * 0.50

        # it checks if the totalPrice is greater than 100 but lesser than 200, it discounts 20%
        if 200 < totalPrice > 100:
            print("----------You got a 20% discount!---------")
            totalPrice = totalPrice * 0.8
        # it checks if the total price is greater than 200, it discounts 40%
        elif totalPrice > 200:
            print("-----------You got a 40% discount!--------")
            totalPrice = totalPrice * 0.6
        # it checks if the price is lesser than 100, it will not give discount.
        elif totalPrice < 100:
            print("----------Sorry. No more discount!----------")

        print("# of Items:                  " + str(len(records)))
        print("Total Price Before Tax:     $" + '{:.2f}'.format(totalPrice))
        print("Total Tax:                  $" + '{:.2f}'.format(totalPrice * 0.13))
        print("Total Price:                $" + '{:.2f}'.format(totalPrice * 1.13))
        customerInfo.close()


store = Store()
item = itemCreation()
item.createTable()
item.insertItem()
customer().itemSelection()
store.__del__()
