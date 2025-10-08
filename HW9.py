#Name:Carlos
#Class: 6th Hour
#Assignment: HW9
import random
#1. Print "Hello World!"
print("hello world")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
rand_num_list = [random.randint(1,100), random.randint(1,100), random.randint(1,100)]
#3. Print the list.
print(rand_num_list)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if rand_num_list[0]>= rand_num_list[1] and rand_num_list[0]>= rand_num_list[2]:
    print(rand_num_list[0], "is the greatest")
    num=rand_num_list[0]
elif rand_num_list[1]>= rand_num_list[0] and rand_num_list[1]>= rand_num_list[2]:
    print(rand_num_list[1], "is the greatest")
    num=rand_num_list[1]
elif rand_num_list[2]>= rand_num_list[0] and rand_num_list[2]>= rand_num_list[1]:
    print(rand_num_list[2], "is the greatest")
    num=rand_num_list[2]
#5. Tie the result (the largest number) from #4 to a variable called "num".

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.
if num%2==0:
    if num%3==0:
        print(num, "is divisible by 2 and 3")
    else:
        print(num, "is divisible by 2 but not 3")
else:
    if num%3==0:
        print(num, "is divisible by 2 and 3")
    else:
        print(num, "is divisible by neither")
