#program to know if the email format is correct or not
email=input("Introduce an email address: ")

count=email.count('@')
count2=email.count('.')


end=email.rfind('@') #final
start=email.find("@")

if(count!=1 or count2<1 or end==(len(email)-1) or start==0):
	print("Wrong email address")	

else:
	print("correct email address")