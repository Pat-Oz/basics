# FILENAME INPUT
filename = raw_input("Enter filename: ")
target = open (filename, 'a')

# USER INPUT
print "Enter first two lines of text:"
line1 = raw_input("Line 1: ")
line2 = raw_input("Line 2: ")

# WRITE INPUT
print "Input text succesfully written to file."
target.write(line1)
target.write("n")
target.write(line2)
target.write("n")

# FILE CREATION CONFIRMATION
print "File succesfully created."
target.close()