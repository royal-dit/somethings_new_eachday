import sys
def prime_num_finder():
    i = 2
    while True:
        try:
            p = int(input("Please enter up to what number the prime numbers should be: "))
            break
        except ValueError:
            sys.stderr.write('ERROR\n')
            sys.stderr.write(' Try again...\n')
    while  i != (p + 1):
        x = i

        if x % 2 and  x % 3 and x % 5 and x % 7 > 0.1: # Checks if the remainder is greater than 0.1 to see if it has an remainder
            r1 = True

        else:
            if i == 2 or i == 3 or i == 5 or i == 7:
                r1 = True
            else:
                r1 = False
        if r1 == True:
            print(i, " is a prime number!")
        else:
            pass
        i = i + 1

prime_num_finder()
quit()