#Task 10 create a class called rectange with a method to calculate the area of the rectangle
class rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def findarea(self):
        area=self.width*self.height
        print('The area of your rectangle is ',area)

h=int(input('Enter the height of your rectangle'))
w=int(input('Enter the width of your rectangle'))

obj1=rectangle(h,w)
obj1.findarea()
