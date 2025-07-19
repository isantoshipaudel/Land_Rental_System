from datetime import datetime
from read import read_file, from_file_read_, land_ID, Costumer_name, date_time_,land_ID_return,Costumer_name_return, date_time_return,userPhone_valid

def Write_Details(Land_dictionary):
    file= open("Land.txt", "w")
    for values in Land_dictionary.values():
        file.write(str(values[0]) + "," + str(values[1]) + "," + str(values[2]) +
                   "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))
        file.write("\n")
    file.close()

#rentInvoice
def write_rent_invoice(valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime, milliseconds):
    with open(str(Name) + str(dateandtime) + ".txt", 'w') as file:
        file.write("\n")
        file.write("-------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t INVOICE\n")
        file.write("\t\t\t\t\t*******************************The Land Management PVT LTD.****************************************\n")
        file.write("\t\t\t\t\t\t 25Street SM Road  |  Branch At Kamalpokhari, Kathmandu, Nepal\n")
        file.write("BILL NO. : " + str(milliseconds) +"\t")
        file.write("Name: " + str(Name) + " \t\t\t\t\t\t\t\t\t\t Bill From: Santoshi Paudel, Land Management Pvt Ltd\n")
        file.write("\t")
        file.write("Phone Number: " + str(Phone_number) + " \t\t\t\t\t\t\t\t\t  Telephone : +12 3965990\n")
        file.write("\t")
        file.write(str(dateandtime) + "\t")
        file.write("\t")
        file.write("\t")
        file.write("--------------------------------------------------------------------------------------------------------------------------------\n")
        
        total = 0  # Initialize total outside the loop
        grand_total = 0
        i = 1  # Initialize i
        for data in Customer_Dictionary:
            file.write("The Kitta Number of the Land:" + str(data[0]) + "\n")
            file.write("The Location of the land:" + str(data[1]) + "\n")
            file.write("The Direction of the land:" + str(data[2]) + "\n")
            file.write("The Anna details of land:" + str(data[3]) + "\n")
            file.write("Monthly Rate of Land:" + str(data[4]) + "\n")
            file.write("Duration of Rent:" + str(data[5]) + "\n")
            file.write("Total Amount:" + str(data[6]) + "\n")
            file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            total += int(data[5])  # Add the duration to the total
            grand_total = grand_total + int(data[6])
            file.write("The Grand Total Amount is " + str(grand_total) + "\n")
            i += 1  # Increment i

        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("CRITERIA: Fund Once Paid Will Not Be Refunded. \n")
        file.write("\t\t\t\t\t\t\t\t      Thank you for dealing with us-)))\n")
        file.write("\t\t\t\t\t\t\t\t   Looking Forward To Deal with You Again!!!\n")
        file.write("\t\t\t\t\t @ if you have any queries about the invoice, Please contact\n")
        file.write("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123\n")
        file.write("************************************************************************************************************************************************************************\n")

#ReturnInvoice

def write_return_invoice(valid_ID, Name, Customer_Dictionary, Phone_number, dateandtime, fine, milliseconds):

    with open(str(Name) + str(dateandtime) + ".txt", 'w') as file:
        file.write("\n")
        file.write("-------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t INVOICE\n")
        file.write("\t\t\t\t\t*******************************The Land Management PVT LTD.****************************************\n")
        file.write("\t\t\t\t\t\t 25Street SM Road  \t |  Branch At Kamalpokhari, Kathmandu, Nepal\n")
        file.write("BILL NO. : " + str(milliseconds) +"\t")
        file.write("Name: " + str(Name) + " \t\t\t\t\t\t\t\t\t\t Bill From: Santoshi Paudel,Land Management Pvt Ltd\n")
        file.write("\n")
        file.write("Phone Number: " + str(Phone_number) + " \t\t\t\t\t\t\t\t\t  Telephone : +12 3965990\n")
        file.write("\t")
        file.write(str(dateandtime) + "\t")
        file.write("\t")
        file.write("\t")
        file.write("--------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("\t")
        total = 0  # Initialize total outside the loop
        grand_total = 0
        
        i = 1  # Initialize i
        for data in Customer_Dictionary:
            file.write("The Kitta Number of the Land is: " + str(data[0]) + "\n")
            file.write("The Location of the land is: " + str(data[1]) + "\n")
            file.write("The Direction of the land is: " + str(data[2]) + "\n")
            file.write("The Anna details of land is: " + str(data[3]) + "\n")
            file.write("Monthly Rate of Land: " + str(data[4]) + "\n")
            file.write("Duration of Rent: " + str(data[5]) + "\n")
            file.write("Total Amount: " + str(data[6]) + "\n")
            file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            file.write("Fine:" +str(data[7]))
            file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            total += int(data[5])  # Add the duration to the total
            grand_total += int(data[6])
            i += 1  # Increment i
        
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("Final Amount: \t\t\t" + str(grand_total) + "\n")
        #file.write("Fine: \t\t\t\t\t\t" + str(fine) + "\n") 
        file.write("******************************************************************************************************************************************************************\n")
        file.write("Grand Total: \t\t\t" + str(grand_total + fine) + "\n") 
        file.write("______________________________________________________\n")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("CRITERIA: Fund Once Paid Will Not Be Refunded. \n")
        file.write("\t\t\t\t\t\t\t\t      Thank you for dealing with us-)))\n")
        file.write("\t\t\t\t\t\t\t\t   Looking Forward To Deal with You Again!!!\n")
        file.write("\n")
        file.write("\t\t\t\t\t @ if you have any queries about the invoice, Please contact\n")
        file.write("\t\t\t\t\t\t\t +12 3456 234, +13 56784 123 \n")
        file.write("************************************************************************************************************************************************************************\n")
