#Task 6 To determine whether a given triangle is equilateral, isosceles or scalene
side1=int(input('Enter the length of the first side of your triangle'))
side2=int(input('Enter the length of the second side of your triangle'))
side3=int(input('Enter the length of the third side of your triangle'))

if((side1==side2) and (side2==side3)):
    print('Equilateral Triangle')
elif((side1==side2)or(side2==side3)or(side3==side1)):
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')
