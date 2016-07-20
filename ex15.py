from sys import argv

script, filename = argv
#uses argv to get a filename
 
txt = open(filename)
#uses open command
print "Here's your file %r:" % filename
print txt.read()
#give a file a command by using a dot or period

print "Type the filename again:"
file_again = raw_input("> ")
#tells the computer to print the same command twice except this time make me write out the file name 

txt_again = open(file_again)
#after name is given write out the file

print txt_again.read()
#uses the previous command to open up the file

#you can open files using python alone

txt_again.close()



