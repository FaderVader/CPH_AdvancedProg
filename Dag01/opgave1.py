# Write a program that takes first name, last name -> print greeting
# calc birth year from age

from datetime import datetime as dateYear
year = int(dateYear.today().strftime('%Y'))

firstName = input("Hello, what is your first name?")
lastName = input(" - and can I ask for the last ?")
fullName = firstName + ' ' + lastName

print(f'Hello {fullName}, welcome to the class')

age = int(input("How old are you?"))
birthYear = year - age

print(f"{fullName}, you were born in {birthYear}, right?")
