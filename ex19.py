def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
#manually puts in the number of cheeses and crackers but is from script

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#we tell the computer the exact numbers we want to put in


cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
#makes the computer do math to see the exact number for each


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
#once again uses math with previous numbers to be added together to get a solid number


#My own one
def kids_and_knives(number_of_kids, number_of_knives):
    print "You have %d kids running around!" % number_of_kids
    print "I know, and they have %d nerf guns!" % number_of_knives

kids_and_knives (50, 60)
number_of_knives = 30
number_of_kids = 50

print "And we can combine the two:"
kids_and_knives(number_of_kids + 20, number_of_knives - 200)




