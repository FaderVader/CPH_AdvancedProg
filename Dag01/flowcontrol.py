if True:
	print('True')
elif not True:
	print('False')
else:
    print("quantum state")

userInput = input("What is your color:") #.lower()
userColor = userInput.lower()
print(userColor)

if userColor == 'red':
    message = "Great color!"
elif userColor == 'blue':
     message = "Like the ocean!"
elif userColor == 'yellow':
     message = "Like the Sun?"
else:  
    message = "Boring...!!!"
print(message)

# truthy
print(False or "Value") # returns Value
print("Yellow" in ["Blue", "Yellow"]) # prints True

# try / except
number = 0
expectedNumber = input('Give me number>') 
try:
    number = int(expectedNumber)
    print(number * number)
    print(3.1456 / number)
except ValueError:
    print("Thats not a number!")
except ZeroDivisionError:
    print("number cannot be 0")
