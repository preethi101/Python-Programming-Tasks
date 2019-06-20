#Task 7 to find the median of three numbers

#Initializing the integer array with 0s
myarray=[0,0,0]
myarray[0]=int(input('Enter the first number'))
myarray[1]=int(input('Enter the second number'))
myarray[2]=int(input('Enter the third number'))
myarray.sort()
print('The median of the three numbers is')
print(myarray[1])
