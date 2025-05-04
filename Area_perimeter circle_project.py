class Circle():
    def __init__(self, radius, perimeter, area):
        self.radius = radius
        self.perimeter = perimeter
        self.area = area
    def get_area(self):
        return self.area
        print("The area of the circle is: ", self.area)