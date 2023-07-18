# DNA PROJECT

## Team 54


* Commands:
    * **SELECT**:
        * **Select all food items at a given price**
        * Query:
            * > `select Food_Name as Food from Food where Price = 35;`
        * The above query selects all the food items with Price equal to 35

        * **Select all the details of the staff working in a certain canteen**
        * Query:
            * > `select SD.Aadhar_Number, SD.Fname, SD.Mname , SD.Lname, SD.Age, SD.Gender from Staff_Details SD, Staff S where S.Aadhar_Number = SD.Aadhar_Number and S.Canteen_Name = "Davids Bakery";`
        * The above query selects details of staff working in David's Bakery 

    * **PROJECT**:
        * **Get the names of all the beverages that cost more than 35**
        * Query:
            * > `select Beverage_Name from Beverages where Price > 35;`
        
        * **Get the details of all the customers older than 19**
        * Query:
            * > `select C.Aadhar_Number,C.Name,C.Date_of_Birth,Cp.Phone_Number from Customer C ,Customer_Ph_Number Cp where C.Aadhar_Number = Cp.Cust_Aadhar and year(curdate()) - year(C.Date_of_Birth) > 19;`
    
    * **AGGREGATE:**
        * **Display AVG cost of a beverage in a canteen**
        * Query:
            * > `SELECT AVG(Price) AS Average_Cost FROM Beverages;` 
        * Let's a Customer know the average price of a beverage in all the canteens

        * **Display MIN salary paid to the staff working in the canteen**
        * Query:
            * > `SELECT MIN(Salary) AS Minimum_Salary FROM Staff;` 
        * Allows the Mess Committe member know the minimum salary paid to a Canteen Staff Member and take appropriate decisions


    * **SEARCH:**
        * **Search for the items in the inventory by the item name and check the quantity remaining**
        * Query:
            * > `SELECT Canteen_Name, Item_Name Total_Quantity_Ordered - Quantity_Utilised AS Quantity_Remaining FROM Inventory;` 
            
        * **Search for the customers with names that start with the letter T**
        * Query:
            * > `SELECT Name FROM Customer WHERE Name LIKE 'T%';`

        * **Search for Company names of length x letters**
        * Query:
            * > `SELECT Name FROM Company WHERE CHAR_LENGTH(Name) = %d;`


    * **INSERT**:
        * **Insert a mess committee member**
        * Query:
            * > `INSERT INTO Mess_Committee(M_ID, Member_Name, Age, Designation) VALUES(53, Lucas, 19, Intern);` 
        * The above query inserts the details of a newly joined Mess Committee member into the Mess_Comm table

        * **Insert a new Canteen**
        * Query:
            * > `INSERT INTO Canteen(Canteen_Name, Location, Year_of_Opening, Opening_Time, Closing_Time, Mess_Manager_ID) VALUES("Your Mom's Kitchen", "Parijaat", 2003, "06:00" , "19:00", 23)";`
        * The above query inserts the details of a newly opened canteen into  the Cannteen table


    * **ANALYSIS:**
        * **Analyse the quantity of an item remaining in order to determine when to place an order to a company**
        * Query:
            * > `SELECT Canteen_Name, Item_Name FROM Inventory WHERE Total_Quantity_Ordered - Quantity_Utilised <= 10;` 

        * **Determine the most popular item from each canteen so canteens can place orders in a more cost efficient manner.**
        * Query:
            * > `SELECT Food_Name, COUNT(*) AS No_of_Orders FROM Serves GROUP BY Food_Name ORDER BY COUNT(*) DESC LIMIT 1;` 

    * **UPDATE:**
        * **Update the cost of a beverage:**
        * Query:
            * > `UPDATE Beverages SET Price = 15  where Beverage_Name = "Tea";` 
        * Updates the cost of a beverage already existing in the table Beverages

        * **Update the dependents of a staff member:**
        * Query:
            * > `UPDATE Dependent SET S_ID = 10005 where Dependent_Name = "Raj";` 
        * Updates the Staff Member a Dependent is related to in case of an incorrect insert
        
    * **DELETE:**
        * **Delete the record of staff not working in a canteen anymore**
        * Query:
            * > `DELETE FROM Staff_Details WHERE Aadhar_Number = 674251239475;` 
        * Deletes the record of a canteen member who no longer works in a canteen

         



        

        
    

        


        


