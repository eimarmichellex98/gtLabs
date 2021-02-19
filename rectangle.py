class Rectangle:
    # member variables
    #height = 0
    #width = 0
    # constructor
    def __init__(self, height, width):
        self.height = height
        self.width = width
    # calculate area
    def area(self):
        a = self.height * self.width
        return a
        # return self.height * self.width - another way
    # calculate perimeter
    def perimeter(self):
        p = (2 * self.height) + (2 * self.width)
        return p

# create instance
r1 = Rectangle(10,35)
r1.height = 20

r2 = Rectangle(2,5)

print("The area of the rectangle is ", r1.area())
print("The area of the 2nd rectangle is ", r2.area())
print("The perimeter of the 2nd rectangle is ", r2.perimeter())

print(f"Area of r1 = {r1.height} x {r1.width} = {r1.area()}")
print(f"Area of r2 = {r2.height} x {r2.width} = {r2.area()}")