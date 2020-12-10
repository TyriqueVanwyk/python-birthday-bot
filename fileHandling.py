import sys

def addBirthday():
	print("")
	print("----------------------------------------------------------------------------------------------------------------------------------------------")
	print("")
	print("Type '0' if you want to cancel and quit")
	print("Person contact Name:")
	contactName = input()
	#Check if the user wants to quit
	if contactName == "0": sys.exit()
	print("Contact number:")
	contactNumber = input()
	#Check if the user wants to quit
	if contactNumber == "0": sys.exit()
	print("Contact birth date (mm/dd format):")
	contactBirthday = input() ## mm/dd format
	#Check if the user wants to quit
	if contactBirthday== "0":sys.exit()

	##Creates a new file if the file does not exist and if the file does exist it appends the file
	f = open("Birthdays.txt", "a")
	f.write("{name}#{birthday}#{number}\n".format(name=contactName, birthday=contactBirthday, number=contactNumber))	
	f.close

def menu():
	print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
	print("						iS The brithday messanger for us who forget birthdays :)")
	print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_")
	print("Select a item from the menu")
	print("1. Add New Birthday")
	print("2. Edit Birthdays")
	print("0. Exit")

	userChoice = input()
	return userChoice
##This function is to make the process of the 'Add new birthday menu' usable in other files
def menuNewBirthday():
	newBday = True
	addBirthday()
	while newBday:
		print("Do you wish to continue? ('y' for yes and 'n' for no and type '0' to exit)")
		userinput = input()
		if userinput.upper() == "Y":
			newBday = True
		elif userinput.upper() == "N":
			newBday = False
			exit
		elif userinput.upper()=="0":
			newBday = False
			menu()
			exit

## use the menu
try:
	userChoice = menu()
	if userChoice == "1":
		##call the function to execute the menu
		menuNewBirthday()

	elif userChoice == "0":
		exit
except:
	print("An error occured")
