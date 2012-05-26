import random

digits = (("0", 1), ("1", 0), ("2", 0), ("3", 0), ("4", 0), ("5", 0), ("6", 1), ("7", 0), ("8", 2), ("9", 1))
composed_number = [] # Hier wird die aus den Ziffern zusammengesetzte Zahl abgelegt
value = 0
while len(composed_number) <= 5:
    r = random.randint(0,9)
    composed_number.append(digits[r][0])
    value = value + int(digits[r][1])
element = (str(composed_number), value)

result = ""
print result.join(composed_number)
for value in element:
    print value
    #print len(element) 
print "Ende" 
