#Task 9 Write a python program to count the number of odd and even numbers in a list

n=int(input('Enter the number of elements in your list'))
mylist=[0 for i in range(n)]
print('Enter the numbers in your list')
odd_count=0
even_count=0
for i in range(n):
    mylist[i]=int(input())
    if(mylist[i]%2!=0):
        odd_count=odd_count+1
    elif(mylist[i]%2==0):
        even_count=even_count+1
print('The number of even numbers is: ',even_count)
print('The number of odd numbers is: ',odd_count)

