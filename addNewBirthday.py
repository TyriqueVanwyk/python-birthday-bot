def addBirthday():
	print("Person contact Name:")
	contactName = input()
	print("Contact number:")
	contactNumber = input()
	print("Contact birth date (mm/dd format):")
	contactBirthday = input() ## mm/dd format
	##Creates a new file if the file does not exist and if the file does exist it appends the file
	f = open("Birthdays.txt", "a")
	f.write("")
	f.write("{name}#{birthday}#{number}\n".format(name=contactName, birthday=contactBirthday, number=contactNumber))	
	f.close

newBday = True
while newBday:
	addBirthday()
	print("Do you wish to continue? ('y' for yes and 'n' for no)")	
	try:
		userinput = input()
		if(userinput == "Y"):
			newBday = True
		elif (userinput == "N"):
			newBday = False 
	except:
		print("An error occured")


