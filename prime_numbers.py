''' Working with prime numbers by setting start value and end value
for desired prime number range '''

number = int(input('Start: ')) # Enter starting value
sec_number = int(input('End: ')) # Enter ending value
for num in range(number, sec_number+1): # Gets range of numbers from start to end
    if num > 1: 
        for i in range(2, num): # Gets range between 2 and num
            if num % i == 0: # Gets the remainder of num divided by i if remainder
                # is zero it means i is a factor of num the code breaks and starts
                # from the first for loop.
                break
        else:
            print(num, end = ', ') # when loop ends and no factors are found betwwen 2 and num, 
            # this else statement is executed.