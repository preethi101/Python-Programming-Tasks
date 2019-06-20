#Task 5 Accept the name of the month and display the number of days
month=input('Enter a month')

if(month=='February'):
    days=29
    print('No. Days is ',days)
elif(month in ['January','March','May','July','August','October','December']):
    days=31
    print('No. Days is ',days)
elif(month in ['April','June','September','November']):
    days=30
    print('No. Days is ',days)
else:
    print('Invalid Month')

