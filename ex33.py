i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num

j = 0
while j < len(numbers):
	print numbers[j]
	j += 1

print "The length of numbers is %d" % len(numbers)

#i has to meet the following statements so it has to be less than six and when you add 1 it equals 6. The system the
