
from datetime import datetime


#Welcome message
def welcome_():
    
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t\t Hello and Welcome to The Land Management System ")
    print("\n")
    print("\t\t\t\t\t\t\t\tThank You For Choosing us. We Look Forward To deal with You:)")
    print("\n")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

def read_file():
    # An empty dictionary is created
    Land_dictionary={}
    file=open("Land.txt","r")
    valid_number=1
    for line in file:
            line = line.replace("\n", "")
            Land_dictionary[valid_number] = line.split(",")
            valid_number += 1
    return Land_dictionary

def from_file_read_():
    i = 1
    file = open("Land.txt", "r")
    print("ID","\t","Kitta Number","\t", "City/District","\t\t", "Direction","\t","Anna","\t\t","Amount","\t","Status")
    print("-------------------------------------------------------------------------------------------------------------------")
    for line in file:
        print(i, "\t "+line.replace(",", "\t\t"))
        i= i+1
    file.close()

# Asking to provide the ID of the Land from the available option
def land_ID():
    while True:
        try:
            print("\n")
            valid_ID = int(input("Can You Please Provide the land ID :"))
            print("\n")

            land_data = read_file()  # Read land data from the file
            if valid_ID <= 0 or valid_ID > len(land_data):
                print("\n")
                print("The Land with the provided ID does not exist!!")
                print("\n")
            else:
                # Check if the land is available
                if land_data[valid_ID][5].strip() == "Available":
                    print("\n")
                    return valid_ID
                else:
                    print("\n")
                    print("The Land with the provided ID is not available for rent.")
        except ValueError:
            print("\n")
            print("Sorry!! You have entered an unavailable id. Try Again!!!")
def land_ID_return():
    while True:
        try:
            print("\n")
            valid_ID = int(input("Could You Please Provide the land ID :"))
            print("\n")

            land_data = read_file()  # Read land data from the file
            if valid_ID <= 0 or valid_ID > len(land_data):
                print("\n")
                print("The Land with the provided ID does not exist!!")
                print("\n")
            else:
                # Check if the land is available
                if land_data[valid_ID][5].strip() == "Not Available":
                    print("\n")
                    return valid_ID
                else:
                    print("\n")
                    print("The Land with the provided ID is Still Available for rent!!You have entered the wrong ID.")
        except ValueError:
            print("\n")
            print("Sorry!! You have entered an unavailable id. Try Again!!!")

#For valid phone number of the user:
def userPhone_valid():
    while True:
        print("\n")
        Phone = input("Input Your Phone Number Please:  ")
        if Phone.strip()=="":
            print("\nINVALID!!! Phone number cannot be empty. Please try again.")
        else:
            try:
                number = int(Phone)
                if number < 0:
                    print("\nINVALID!!! Phone number cannot be negative. Please try again.")
                else:
                    return Phone
            except ValueError:
                print("\nINVALID!! Please Check And Try Again :))")




def Costumer_name():
    while True:
        print("\n")
        Name = input("Please Input Your Name To Continue the Rental process: ")
        if Name.strip()== "":
            print("\nINVALID!!! Name cannot be empty. Please try again.")
        else:
            try:
                int(Name)
                print("\nINVALID!!! Name cannot be numeric. Please try again.")
            except ValueError:
                return Name


# Asking to input the costumer name if he/she wishes to rent
def Costumer_name_return():
   while True:
        print("\n")
        Name = input("Please Input Your Name To Continue the Return the Land: ")
        if Name.strip()== "":
            print("\nINVALID!!! Name cannot be empty. Please try again.")
        else:
            try:
                int(Name)
                print("\nINVALID!!! Name cannot be numeric. Please try again.")
            except ValueError:
                return Name



def date_time_():
    dateandtime = datetime.now()
    str_date_time = str(dateandtime)
    print("Date and Time:"+ str_date_time)
    return str_date_time
    

def date_time_return():
    dateandtime = datetime.now()
    str_date_time = str(dateandtime)
    print("The date and time of Returning Land is:"+ str_date_time)
    return str_date_time


        

