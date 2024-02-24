name = input("what is your name: ")
surname = input("what is your surname: ")
from datetime import date
date_of_birth = int(input("what year where you born: "))
today_time = date.today().strftime("%Y")
print("users full name is" + " " + name + " " + surname + " " + "and is",int(today_time)-date_of_birth)



