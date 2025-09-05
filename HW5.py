#Name:Carlos L
#Class: 6th Hour
#Assignment: HW5


#1. Create a list with 9 different numbers inside.`
num_list = [6,7,3,8,1,9,2,4,5,]
#2. Sort the list from highest to lowest.
num_list.sort(reverse=True)
#3. Create an empty list.
empty_list = []
#4. Remove the median number from the first list and add it to the second list.
empty_list.append(num_list[4])
empty_list.remove(num_list[4])
#5. Remove the first number from the first list and add it to the second list.
empty_list.append(num_list[0])
empty_list.remove(num_list[0])
#6. Print both lists.
print(empty_list)
print(num_list)
#7. Add the two numbers in the second list together and print the result.
print(empty_list[4] + empty_list[0])
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).

#9. Sort the first list from lowest to highest and print it.
empty_list.sort()