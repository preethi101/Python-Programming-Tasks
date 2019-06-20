#Task 2 accept the file name and display the extension
filename=input('Input the filename')
file_extensions=filename.split(".")
print('The extension of the file is: ' + repr(file_extensions[-1]))
