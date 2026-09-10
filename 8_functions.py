
number = int(input('Enter a number to find its factorial: '))

def  factorial(number):

    fact = 1;
    if number <= 1:
        return  fact

    else:
        for i in range(1, number+1):
            fact = fact * i
        return fact

print("The factorial is ", factorial(number))