#Task 3- Accept a list of words and print the length of the longest one
n=int(input('Enter the number of words in your list'))
print('Enter the words in your list')
L=["" for x in range(n)]
for i in range(n):
    L[i]=input()
longest=len(L[0])
for i in range(n):
    if(longest<len(L[i])):
        longest=len(L[i])
print(longest," is the length of the longest word")
