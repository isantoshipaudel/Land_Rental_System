from read import read_file, from_file_read_, land_ID, Costumer_name, date_time_,land_ID_return,Costumer_name_return, date_time_return,userPhone_valid, welcome_
from operation import rent_land, return_land
from write import write_rent_invoice, write_return_invoice

Land_dictionary=read_file()
welcome_()

def Choose_option():
    Continuous_loop=True
    while Continuous_loop== True:
        print("\n  a)Enter 1 to Rent land")
        print("\n  b)Enter 2 to Return land")
        print("\n  c)Enter 3 to Exit")
        print("\n")
        

        Choose_option=True
        while Choose_option==True:
            try:
                option_input= int(input(" Please Enter an Available Value Either to Rent Land or Return Land or Exit :"))
                print("\n")

                Choose_option=False
            except:
                print("Enter only available numbers not Alphabetical values!!")
        
                 
        if option_input==1:
            from_file_read_()
            not_available = all(data[5] == "Not Available" for data in Land_dictionary.values())
            if not_available:
                print("Sorry!! All Lands are Rented out.")
            else:
                print("----------------------------Lands are Available!!! Please choose the Available Option----------------")
                valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime, milliseconds =rent_land()
                write_rent_invoice(valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime,milliseconds )
            
    
        elif option_input==2:
            from_file_read_()
            available = all(data[5] == "Available" for data in Land_dictionary.values())
            if available:
                print("Sorry!!Lands are not Rented out. You cannot return without renting.")
            else:
                print("------------------------Lands Can be Returned only If It is Rented i.e, Status is UnAvailable!!------------------------")
                valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime, fine, milliseconds =return_land()
                write_return_invoice(valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime, fine, milliseconds)


        elif option_input == 3:
            print("THANK YOU FOR USING OUR LAND MANAGEMENT SYSTEM!!!")
            Continuous_loop = False
        else:
            print("Invalid!!! Please Enter the value as either 1 or 2 or 3")

Choose_option() 
            
