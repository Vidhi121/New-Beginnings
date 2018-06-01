 '''This solves the Collatz Conjecture and gives us the count of recursions
    taken to reach 1. '''

def coltz(num, count = 0):
    if num<=1:
        return count      #Final condition
    if num%2==0:
        return coltz(num/2, count+1)      #even, try to reach 1
    else:
        return coltz(num*3+1, count+1)    #odd, try to reach 1

#Test runs
print coltz(2) # count = 1
print coltz(3) # count = 7
print coltz(4) # count = 2
