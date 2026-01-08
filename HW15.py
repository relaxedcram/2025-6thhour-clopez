#Name:
#Class: 6th Hour
#Assignment: HW15

#1. import the "random" library
import random
#2. print "Hello World!"
print('hello world')
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
variable_A = int(input('Enter a number: '))
variable_B = int(input('Enter a number: '))
variable_C = int(input('Enter a number: '))
#4. Add a and b together, then divide the sum by c. Print the result.
variable_A += variable_B // variable_C
#5. Round the result from #3 up or down, and then determine if it is even or odd.
print(round(variable_A))
#6. Create a list of five different random integers between 1 and 10.
num_list = [4,1,2,6,8]
print(random.choice(num_list))
#7. Print the 4th number in the list.
print(num_list[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
num_list.append(7)
print(num_list)
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
num_list.sort()
print(num_list)
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1

while i <= 100:
    print(i)
    i = i + i
#11. Create a list containing the names of five other students in the classroom.
names_list=['Greg','Ethan','Ally','Shane','Aaden']
#12. Create a for loop that individually prints out the names of each student in the list.
for names in names_list:
    print(names)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for j in range(1, 101):
    if j % 10 == 0:
        print(j)