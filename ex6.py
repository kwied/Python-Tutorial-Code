x = "There are %d types of people." % 10
# d represents the variable of 10
binary = "binary"
#shows what the variables each mean for the following string
do_not = "don't"
y = "Those who knwo %s and those who %s." % (binary, do_not)

print x
# re-prints the previous statements
print y

print "I said: %r." % x
#once again shows what each variable represents
#string in a string
print "I also said: '%s'." % y

hilarious = False
# shows the variables for the following string of print joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
#adds the variables together to create a string 
#it's shorthand!
#makes a longer stirng since it takes each individual stirng and adds them together to create one long string

