# Recursively returns the present term and the future term in the Fibonacci sequence.
    
def fib(n):
    if n == 1:
        return [1, 0]
    else:
        terms = fib(n - 1)
        terms = [terms[0] + terms[1], terms[0]]
        return terms


def is_pos():      #takes input from user and returns when number is positive and less than 500
    while True:
        s = raw_input(" Which term in the Fibonacci sequence do you want to see? ")
        try:
            n = int(s)
            if n >= 500:
                print "Please enter number less than 500!"
            elif n > 0:
                return n
            else:
                print "Enter a positive integer!"

        except ValueError:
            print "Enter a positive integer."


def main():
    n = validate_positive_integer()
    print fib(n)[1]


if __name__ == "__main__":
    main()
