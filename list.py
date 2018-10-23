import random
def ListManipulation():
    length = input( "Please enter the length for the list: ")
    low = input( "Please enter the lower bound for the range of integer values: ")
    high = input( "Please enter the upper bound for the range of integer values: ")
    res = [] 
    max = low
    min = high
    sum = 0
    
    for j in range(length): 
        num = random.randint(low, high)
        res.append(num) 
        if max < num:
            max = num
        if min > num:
            min = num
        sum = sum + num
    print ("Sequence: "),
    print(res)
    print "List length: " + str(length)
    print "Largest integer: " + str(max)
    print "Smallest integer: " + str(min)
    print "Sum: " + str(sum)
    print "Average: " + str(sum / length)
ListManipulation()