#Name:Carlos L
#Class: 6th Hour
#Assignment: HW7

#1. Print Hello World!
print('hello world')
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
numbers = {
"number1" : "3",
"number2" : "6",
"number3" : [7,6,2],}
#3. Print the keys of the dictionary from #2.
print(numbers.keys())
#4. Print the values of the dictionary from #2
print(numbers.values())
#5. Print one of the three numbers from the list by itself
print(numbers["number3"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
numbers . update({"number4" : 9})
#7. Print the entire dictionary from #2 with the updated key and value.
print(numbers)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.

#9. Print the names of all three classmates on the same line.

#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.