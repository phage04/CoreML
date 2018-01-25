#Arrays
array = ["lyle", "jover"]
array[0] = "bob"
print(array[0] + " " + array[1])

groceryArray = ["eggs", "milk", "cheese", "kombucha", "coffee", "aligator jerky"]
listSlice = groceryArray[3:5]
sliceUpToThree = groceryArray[:3]
sliceFromThreeOn = groceryArray[3:]
sliceSecondFromEnd = groceryArray[-2]
print(listSlice)
print(groceryArray)
print(sliceUpToThree)
print(sliceFromThreeOn)
print(sliceSecondFromEnd)

#Tuples
(xValues, yValues) = ([1, 2, 3], [-1, -2, -3])
print("PLOT THIS POINT: ", xValues[2]," ",yValues[0])

tuple = (xValues, yValues)
print(tuple[0][1])
