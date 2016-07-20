from sys import argv
#import is how you add features but still keep the code small
#argv is the argument variable 
#argv assigns arguments to four different variables (it unpacks everything)

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", raw_input("What do you do? ")
print "Your second variable is:", second
print "Your third variable is:", third

script = raw_input("What do you do? ")
first = raw_input("Who is your sister? ")
second = raw_input("Who is your brother? ")

