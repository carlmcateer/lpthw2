# from the sys module import the argv function, this allows us to take command line arguents
from sys import argv

# Allocate argv to the variables script and filename
script, filename = argv

#Asign to the var txt the result of the open function on the file is called from argv
txt = open(filename)

# Prints a string and inserts the name of the file from the argv
print "Here's your file %r:" % filename
# Print the result of running the .read() function on txt
print txt.read()

txt.close()
# Print string to the screen
print "Type that filename again:"
# Prompt the user to input the file name and assign it to the var "file_again"
file_again = raw_input("> ")

# Asign to the var "txt_again" the result of the open function on the file that the user typed in
txt_again = open(file_again)

# Print to the screen the contence of the file that the user was prompted to type
print txt_again.read()
txt_again.close()
