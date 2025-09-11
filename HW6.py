#Name:Carlos L
#Class: 6th Hour
#Assignment: HW6


#1. Import the "random" library
import random
from random import shuffle

#2. print "Hello World!"
print('hello world')
#3. Create three different variables that each randomly generate an integer between 1 and 10
random_number1 = random.randint(1,10)
random_number2 = random.randint(1,10)
random_number3 = random.randint(1,10)
#4. Print the three variables from #3 on the same line.
print(random_number1, random_number2, random_number3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
random_number1+=2
random_number2-=4
random_number3x=1.5
#6. Print each result from #5 on the same line.
print(random_number1, random_number2, random_number3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
num_list=[random . randint(1,6),random . randint(1,6),random . randint(1,6),random . randint(1,6)]
#8. Sort the list in #7 and print it.
num_list.sort()
print(num_list)
#9. Add together the highest three numbers in the list from #7 and print the result.
print(num_list[1]+num_list[2]+num_list[3])
#10. Create a list with 5 names of other students in this class and print the list.
people_list =['eli','devon','carlos','tristan','greg']
print(people_list)
#11. Shuffle the list in #10 and print the list again.
random . shuffle(people_list)
print(people_list)
#12. Print a random choice from the list of names from  #10.
print(random.choice(people_list))