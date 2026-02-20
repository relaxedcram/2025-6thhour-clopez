#Name: Carlos
#Class: 6th Hour
#Assignment: HW20

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class Items:
    def __init__(self,stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight
    def double(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
Doc = Items(1, 120, 200)
Warden = Items(5, 100, 180)
Ash = Items(10, 50, 150)
#3. Print the stock of all three objects and the cost of the second store item.
print(Doc.stock, Doc.cost, Doc.weight)
print(Warden.stock, Warden.cost, Warden.weight)
print(Ash.stock, Ash.cost, Ash.weight)
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
Warden.double()
print(Warden.cost)
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.

#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del Doc
