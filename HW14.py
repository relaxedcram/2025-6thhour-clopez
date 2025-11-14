#Name:Carlos L
#Class: 5th Hour
#Assignment: HW14


#1. Create a for loop with variable i that counts down from 5 to 1 and then prints "Hello World!"
#at the end.
for i in range(5, 0, -1):
    print(i)
print("Hello World!")
#2. Create a for loop that counts up and prints only even numbers between 1 and 30.
for number in range(0, 30, 2):
    print(number)
#3. Create a for loop that prints from 1 to 30 and continues (skips the number) if the number is
#divisible by 3.
for j in range(1, 31):
    if j % 3 == 0:
        continue
    print(j)
#4. Create a for loop that prints 5 different animals from a list.
animal_list=["dog","cat","cow","lizard","fish"]
for animal in animal_list:
    print(animal)
#5. Create a for loop that spells out a word you input backwards.
#(HINT: Google "How to reverse a string in Python")
for k in input('Enter your name: ') [::-1]:
    print(k)
#6. Create a list containing 10 integers of your choice and print the list.
integer_list = [12, 24, 31, 47, 59, 67, 76, 82, 93, 10]
print(integer_list)
#7. Create two empty variables named evenNumbers and oddNumbers.
evenNumbers = 0
oddNumbers = 0
#8. Make a loop that counts the number of even and odd numbers in the list, and prints the
#result after the loop.
for l in integer_list:
    if l % 2 == 0:
        evenNumbers += 1
    else: oddNumbers += 1
print(evenNumbers, oddNumbers)
#9. Create a variable that asks the user for an integer and an empty integer variable.
m = int(input('Enter a number: '))
n = 1
#10. Create a loop with a range from 1 to the number the user input. Use the loop to find the
#factorial of that number and print the result. A factorial of a number is that number multiplied
#by every number before it until you reach 1. (For example: 5! is 5 x 4 x 3 x 2 x 1 = 120)
for o in range(1, m + 1):
    n *= o
print(n)