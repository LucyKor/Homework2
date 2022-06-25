height_c = int(input("Insert height:"))
side_c = int(input("Insert side length:"))

def content(x):
    print(height_c * side_c / 2)

if (height_c == 10 and side_c == 4):
    print("The content of the triangle is: 20 ")
else:
    print("Incorrect data.")
