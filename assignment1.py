# 1) Write a program that takes two numbers as input and prints their sum

'''first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
sum = first_number + second_number
print("Sum of these two numbers is: ", sum)'''


# 2) WAP that checks whether a given number is even or odd

'''num = int(input("Enter the number:"))
if(num % 2 == 0):
    print("Number is even!!")
else:
    print("Number is odd!!")'''


# 3) WAP that calculates the factorial of a given number

'''num = int(input("Enter the number:"))
fac = 1
while(num>0):
    fac=fac*num
    num=num-1
print("Factorial of number is : ", fac)'''


# 4) WAP that asks the user for their name and then printts a greeting message

'''name = str(input("Enter your name: "))
print("Welcome!! ",name)'''


# 5) WAP that takes a string input from the user and writes it to a text file

# 6) Write a program that reads the content of a text file and prints it to the console.

# 7) Write a python program that takes a string as input and returns its length

'''string = str(input("Enter the string : "))
print(string)
print(len(string))'''


# 8) Write a python program that concatenates two strings and returns the result.

'''first_str = str(input("Enter your first string : "))
second_str = str(input("Enter your second string : "))

message = first_str + second_str

print("Message is : ", message)'''


# 9) Write a python program that checks if a substring is present in a given string.

# using find method

'''
string = 'This is my 9th python program'
print(string.find('is'))
'''

# 10) WAP in python that converts a given string to uppercase

'''string = "hello world"
print(string.upper())'''

# 11) Write a python program that generates the first n numbers in the Fibonacci sequence

'''def fibonacci_numbers(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        # printing fibonacci numbers
        return fibonacci_numbers(num-2)+fibonacci_numbers(num-1)
 
 
n = int(input("Enter the number : "))
for i in range(0, n):
    print(fibonacci_numbers(i), end=" ")'''

# 12) Write a python program that calculates the sum of the digits of a given number.

def getSum(n):   
    sum = 0
    for digit in str(n):  
      sum += int(digit)       
    return sum
   
n = int(input("Enter the number : "))
print(getSum(n))

# 13) Write a program that asks the user for their birth year and calculates their age.

# 14) 

#15)

#16)
string = "Yolo Life"

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")



#17)
my_string = "hello world"

print(my_string[0].upper() + my_string[1:])


#18)
def check(s1, s2):
	
	# the sorted strings are checked 
	if(sorted(s1)== sorted(s2)):
		print("The strings are anagrams.") 
	else:
		print("The strings aren't anagrams.")		 
		 
s1 ="listen"
s2 ="silent"
check(s1, s2)


#19)

#20)
test_list = [12, 67, 98, 34]

print("The original list is : " + str(test_list))

res = []
for ele in test_list:
    sum = 0
    for digit in str(ele):
        sum += int(digit)
    res.append(sum)

print ("List Integer Summation : " + str(res))


#21)
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
count = 0  
for item in my_list:  
  if(item == 5):  
   count += 1  
print(count)


#22)
List_A = [5, 9, 13]
List_B = [7,-3 ,11]
Combined_list = List_A + List_B
#with the functions, the user can get the small and high values
maximum_value = max(Combined_list)
minimum_value = min(Combined_list)
#Output is printed using print function
print("Maximum Value:", maximum_value)
print("Minimum Value:", minimum_value)


#23)
fahrenheit = float(input("Enter temperature in fahrenheit: "))

celsius = (fahrenheit - 32)/1.8

print(str(fahrenheit )+ " degree Fahrenheit is equal\
to " + str(celsius ) + " degree Celsius." )


#24)
n1 = float(input("Enter the First Number: "))
n2 = float(input("Enter the Second Number: "))

#addition

print("{} + {} = ".format(n1, n2))
print(n1 + n2)

#subtraction

print("{} - {} = ".format(n1, n2))
print(n1 - n2)

#multiplication

print("{} * {} = ".format(n1, n2))
print(n1 * n2)

#division

print("{} / {} = ".format(n1, n2))
print(n1 / n2)


#25)
print("Enter the Name of Source File: ")
sFile = input()
print("Enter the Name of Target File: ")
tFile = input()

fileHandle = open(sFile, "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open(tFile, "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()

print("\nFile Copied Successfully!")



#26)
text = "Python is easy to learn."

result = text.startswith('is easy')
# returns False
print(result)

result = text.startswith('Python is ')
# returns True
print(result)

result = text.startswith('Python is easy to learn.')
# returns True
print(result)




#27)
s = "Geeks for"
x = list(s) 
print(x) 

 
 

