//Q1
def convert_days(days):
    years=days//365
    weeks=(days%365)//7
    remaining_days=(days%365)%7
    return years, weeks,remaining_days
    total_days=int(input("Enter the total number of days"))
    years,weeks,remaining_days=convert_days(total_days)
print(f"{days_input} days is equivalent to {years_output} years, {weeks_output} weeks, and {days_output} days.")

//Q2
def check_number(number):
    if number==0:
        print("even")
        elif(number>0):
            if(number%2==0):
                print("positive integer")
    else:
        if(number%2==0):
            print("Negative Even")
        else:
            print("Negative odd")

number_input=int(input("Enter an integer:"))
check_number(number_input)

//Q3
def print_numbers(divisor):
    for number in range(1,101):
        if number % divisor==3:
            print(number)

divisor_input=int(input("Enter a divisor:"))
print(f"Numbers between 1 and 100 divisible by {divisor_input} with a remainder of 3:")
print_numbers(divisor_input)

//Q4
def divide_with_remainder(number1,number2):
    quotient=number1 // number2
    remainder=number1 % number2

    if(remainder==3):
        print(f"The remainder of {number1} divided by {number2} is 3.")
    else:
        print(f"The remainder of {number1} divided by {number2} is not 3.")
        
number1_input=int(input("Enter the first number:"))
number2_input=int(input("Enter the second number:"))
divide_with_remainder(number1_input,number2_input)

//Q5
def calculate_sum():
    S=0.0
    for numberin range(1,51):
        S+=1/number
    return S
sum_value=calculate_sum()
print(f"The value of S is: {sum_value:.4f}")

