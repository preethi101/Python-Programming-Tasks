#Task 8: Write a python function to multiply all the numbers in a list

def multiplyFun(intarray,n):
    multiply=1
    for i in range(n):
        multiply=multiply*intarray[i]
    print('When you multiply all the elements you get ',multiply)

n=int(input('Enter the number of elements in your list'))
mylist=[0 for i in range(n)]
print('Enter the numbers in your list')
for i in range(n):
    mylist[i]=int(input())
multiplyFun(mylist,n)
