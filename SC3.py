#Name:CarlosL`
#Class: 6th Hour
#Assignment: SC3

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all,  the ratings.
player = int(input("enter number of players: "))
total=0
for i in range(1, player+1):
    rate = int(input("enter rate 1-5 "))

    while rate<1 or rate>5:
        print("answer invalid")
        rate = int(input("enter rate 1-5 "))
    else:
        total+=rate

average = total/player

print("the average is",average)