def calculate():
    x = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication 
/ for division
''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if x == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif x == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif x == '*':
        print('{} {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif x == '/':
        if number_2 == 0:  # always check for division by zero
            print("Can't divide by zero, please pass a valid divisor")
        else:
            print('{} / {} = '.format(number_1, number_2))
            print(number_1 / number_2)

    else:
        print(
            'You have not typed a valid operator, please run the program again.')
        exit()
    again()


# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
       Type y to calculate again, type n to end the program
       ''')

    # If the user types Y, run the calculate() function
    if calc_again == 'y':
        calculate()

    # If the user types N, say Good-bye to the user and end the program
    elif calc_again == 'n':
        print('Good-bye')

    # If the user presses another key, run the function again
    else:
        again()


if __name__ == "__main__":
    calculate()
