import phonebook_dir
#this section is for connecting our algorithym and code via re-assigning variables
AA = phonebook_dir.contact_1 
BB = phonebook_dir.contact_2 
CC = phonebook_dir.contact_3 
DD = phonebook_dir.contact_4 
EE = phonebook_dir.contact_5 
# these variables will allow our user to access the database and recieve the information in our source code
#our if and else statements allow us based on our choices to get different results
print ()
choice = (input ("who are you looking for today :D"))
if choice == "AA":
    print ("Here is your info! :)", AA)

elif choice == "BB":
    print ("Here is your info! :)", BB)

elif choice == "CC":
    print ("Here is your info! :)", CC)

elif choice == "DD":
    print ("Here is your info! :)", DD)

elif choice == "EE": 
    print ("Here is your info! :)", EE)

else:
    print ("We could not find who you were looking for. Please try again D:")

#was thinking of making a story off of this but that would take too much time :(