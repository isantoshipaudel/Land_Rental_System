
from datetime import datetime
from read import read_file, from_file_read_, land_ID, Costumer_name, date_time_,land_ID_return,Costumer_name_return, date_time_return,userPhone_valid
from write import Write_Details
Land_dictionary = {}



def rent_land():
    # when the user enter the option to rent land
    Customer_Dictionary=[]# Dictionary to store costumer information
    Loop=True
    print("\t")
    print("---------------------------- Thank You For Choosing Us ))----------------------------------------------------------")
    Land_dictionary=read_file()
    print("\n")
    print("\n \n Provide us your Name, Phone Number and All the Details Asked Below-))  \n \n")
    Name=Costumer_name()
    Phone_number=userPhone_valid()
    #for showing the land available for rent
    print("-------------------------------------------------------------------------------------------------------------------")
    from_file_read_()
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t  We are Carrying out your Rental Process \t\t\t\t\t\t\t\t\t\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("\n")

    while Loop:  # While Loop is True
        valid_ID = land_ID()
        print("\n")
        while True:
            print("\n")
            Time = input("Enter the number of months you want to rent the land:")
            if Time.strip() == "":
                print("\nINVALID!!! Time cannot be empty. Please try again.")
            else:
                try:
                    number = int(Time)
                    if number < 1:
                        print("\nINVALID!!! Number of months cannot be zero or negative. Please try again.")
                    else:
                        print("")
                        break
                except ValueError:
                    print("\nINVALID!! Please Check And Try Again :))")


        Kitta_number = Land_dictionary[valid_ID][0]
        Monthly_Price = int(Land_dictionary[valid_ID][4])  # Convert Monthly_Price to integer
        Total_price = Monthly_Price * int(Time)
        City_District = Land_dictionary[valid_ID][1]
        Direction = Land_dictionary[valid_ID][2]
        Anna = Land_dictionary[valid_ID][3]
        Land_dictionary[valid_ID][5] = "Not Available"
        Write_Details(Land_dictionary)
        milliseconds = datetime.now().timestamp () * 100

        Customer_Dictionary.append([Kitta_number, City_District, Direction, Anna, Monthly_Price, Time, Total_price])
      
        Another_land = input("Do you want to rent another land?? (y/n):").lower()  # Call lower() method
        if Another_land == "y":
            print("-------------------------------------------------------------------------------------------------------------------")
            from_file_read_()
            print("\n")
            print("-------------------------------------------------------------------------------------------------------------------")
            Loop = True
        else:
            Loop = False

        all_not_available = all(data[5] == "Not Available" for data in Land_dictionary.values())
        if all_not_available:
            print("Sorry!! All Lands are Rented out.")
            Loop = False
        
            

    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t INVOICE")
    print("\t")
    print("\t\t\t\t\t*******************************The Land Management PVT LTD.****************************************")
    print("\t")
    print("\t\t\t\t\t\t 25Street SM Road  |  Branch At Kamalpokhari, Kathmandu, Nepal")
    print("\t")
    print("BILL NO. : " + str(milliseconds))
    print("Name: " + str(Name)+ " \t\t\t\t\t\t\t\t\t\t Bill From: Santoshi Paudel,Land Management Pvt Ltd")
    print("\t")
    print("Phone Number: " + str(Phone_number) + " \t\t\t\t\t\t\t\t\t  Telephone : +12 3965990")
    dateandtime=date_time_()
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    total = 0  # Initialize total outside the loop
    grand_total=0
    i= 1  # Initialize i
    for data in Customer_Dictionary:
        print("The Kitta Number of the Land:" + str(data[0]))
        print("The Location of the land:" + str(data[1]))
        print("The Direction of the land:" + str(data[2]))
        print("The Anna details of land:" + str(data[3]))
        print("Monthly Rate of Land:" + str(data[4]))
        print("Duration of Rent:" + str(data[5]))
        print("Total Amount:" +str(data[6]))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        total += int(data[5])  # Add the duration to the total
        grand_total =grand_total+ int(data[6])
        i += 1  # Increment i

    print("\n")
    print("The Grand Total Amount is " + str(grand_total))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("CRITERIA: Fund Once Paid Will Not Be Refunded. ")
    print("\t")
    print("\t\t\t\t\t\t\t\t      Thank you for dealing with us-)))")
    print("\t\t\t\t\t\t\t\t   Looking Forward To Deal with You Again!!!")
    print("\t")
    print("\t")
    print("\t\t\t\t\t @ if you have any queries about the invoice, Please contact")
    print("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 ")
    print("************************************************************************************************************************************************************************")
                
    return valid_ID, Name, Customer_Dictionary,Phone_number,dateandtime, milliseconds


#when the user enter option 2
def return_land():
    # when the user enter the option to rent land
    Customer_Dictionary=[]# Dictionary to store costumer information
    Loop=True
    Land_dictionary=read_file()
    print("\n")
    print("\n \n Provide us your Name, Phone Number and Every Details Asked So That We Can Help You Return The Land   \n \n")
    Name=Costumer_name_return()
    Phone_number=userPhone_valid()
    #for showing the land available for return
    print("-------------------------------------------------------------------------------------------------------------------")
    from_file_read_()
    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t  We are Carrying out the Process So That the Land gets Return  \t\t\t\t\t\t\t\t\t\t")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("\n")

    while Loop:  # While Loop is True
        
        valid_ID = land_ID_return()
        print("\n")
        while True:
            print("\n")
            Time = input("Enter the number of months you have rent the land:")
            if Time.strip() == "":
                print("\nINVALID!!! Time cannot be empty. Please try again.")
            else:
                try:
                    number = int(Time)
                    if number < 1:
                        print("\nINVALID!!! Number of months cannot be Zero or negative. Please try again.")
                    else:
                        print("")
                        break
                except ValueError:
                    print("\nINVALID!! Please Check And Try Again :))")
        while True:
            print("\n")
            Time_return=input("In How Many Month have you return the Land?:")
            if Time_return.strip() == "":
                print("\nINVALID!!! Time cannot be empty. Please try again.")
            else:
                try:
                    number = int(Time_return)
                    if number < 1:
                        print("\nINVALID!!! Number of months cannot be Zero or negative. Please try again.")
                    else:
                        print("")
                        break
                except ValueError:
                    print("\nINVALID!! Please Check And Try Again :))")

        Kitta_number = Land_dictionary[valid_ID][0]
        Monthly_Price = int(Land_dictionary[valid_ID][4])  # Convert Monthly_Price to integer
        Total_price = Monthly_Price * int(Time_return)
        City_District = Land_dictionary[valid_ID][1]
        Direction = Land_dictionary[valid_ID][2]
        Anna = Land_dictionary[valid_ID][3]
        Land_dictionary[valid_ID][5] = "Available"
        Write_Details(Land_dictionary)
        milliseconds = datetime.now().timestamp () * 100
        if Time<Time_return:
            month_delayed=int(Time_return)-int(Time)
            fine= (10/100)*(month_delayed*Monthly_Price)
            print("\t")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        else:
                fine=0
        Customer_Dictionary.append([Kitta_number, City_District, Direction, Anna, Monthly_Price, Time, Total_price,fine])
        Another_land = input("Do you want to return another land?? (y/n):").lower()  # Call lower() method
        if Another_land == "y":
            print("-------------------------------------------------------------------------------------------------------------------")
            from_file_read_()
            print("\n")
            print("-------------------------------------------------------------------------------------------------------------------")
            Loop = True
        else:
            Loop = False
        
        available = all(data[5] == "Available" for data in Land_dictionary.values())
        if available:
            print("Sorry!! All Lands are not Rented out. You cannot return without renting.")
            Loop = False
        
        

    print("\n")
    print("-------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t INVOICE")
    print("\t")
    print("\t\t\t\t\t*******************************The Land Management PVT LTD.****************************************")
    print("\t")
    print("\t\t\t\t\t\t 25Street SM Road  \t |  Branch At Kamalpokhari, Kathmandu, Nepal")
    print("\t")
    print("BILL NO. : " + str(milliseconds))
    print("Name: " + str(Name)+ " \t\t\t\t\t\t\t\t\t\t Bill From: Santoshi Paudel,Land Management Pvt Ltd")
    print("Phone Number: " + str(Phone_number) + " \t\t\t\t\t\t\t\t\t  Telephone : +12 3965990")
    dateandtime=date_time_return()
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    total = 0  # Initialize total outside the loop
    grand_total=0
    
    i= 1  # Initialize i
    for data in Customer_Dictionary:
        print("The Kitta Number of the Land:" + str(data[0]))
        print("The Location of the land:" + str(data[1]))
        print("The Direction of the land:" + str(data[2]))
        print("The Anna details of land:" + str(data[3]))
        print("Monthly Rate of Land:" + str(data[4]))
        print("Duration of Rent:" + str(data[5]))
        print("Total Amount:" +str(data[6]))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("Fine:" +str(data[7]))
        print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        total += int(data[5])  # Add the duration to the total
        grand_total =grand_total+ int(data[6])
        
        i += 1  # Increment i
    print("\n")
    print("Final Amount: " + "\t\t\t" + str(grand_total))
    #print("Fine:" + "\t\t\t" + str(fine))
    print("******************************************************************************************************************************************************************")
    print("Grand Total:" + "\t\t\t" + str(grand_total + fine))#grand total
    print("\n")

    print("\t")              
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("CRITERIA: Fund Once Paid Will Not Be Refunded. ")
    print("\t")
    print("\t\t\t\t\t\t\t\t      Thank you for dealing with us-)))")
    print("\t\t\t\t\t\t\t\t   Looking Forward To Deal with You Again!!!")
    print("\t")
    print("\t")
    print("\t\t\t\t\t @ if you have any queries about the invoice, Please contact")
    print("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 ")
    print("************************************************************************************************************************************************************************")
            
    return valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime, fine, milliseconds 


            
    
        
        
        
        
