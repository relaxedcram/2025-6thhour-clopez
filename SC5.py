#Name:Carlos
#Class: 5th Hour
#Assignment: SC5
from SC4 import *
#Import all of SC4 here


listAverage = 0

def final_average():
    global listAverage
    listAverage =  sum(statblock)/len(statblock)   #Calculate the sum of the list by the length of the list here
    return listAverage

final_average()

print(listAverage)