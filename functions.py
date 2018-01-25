#Conditionals
number = 8

if number > 10:
    print("this number is greater than 10")
else:
    print("this number is less than 10")

if 10 < 100:
    print("Yup")

#Functions
def namePrinter(name, value):
    print(name, value)

namePrinter("Lyle", 123)

#ForLoops
for i in [1, 2, 3, 4, 5]:
    print("Value: ", i)

for i in range(20):
    print(i)

#WhileLoops
x = 10
while x > 0:
    print("x is still greater than zero")
    x = x-1
print(x)

print(x)
