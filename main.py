number_in = input('Enter a number to convert to binary: ')
number_in = int(number_in)

exponent = 0  # set initial value
while (2 ** exponent) <= number_in:  # WHILE loop will continue until 2exp is more than the number
    exponent = exponent + 1  # Systemically adds 1 to the exponent for the next iteration

high_exponent = exponent - 1

remaining_value = number_in  # Create a variable to keep track of the remainder each time through the loop
binary_equiv = ''  # Create an empty string
for a in range(high_exponent, -1, -1):  # FOR loop will start at highest usable exponent, then step down by 1. The value of a the last time through the loop will be 0.
    binary_position_value = 2 ** a  # This variable will be 2 to the current exponent
    if binary_position_value <= remaining_value:  # Checks if the current exponent of 2 is less than or equal to the remaining value.
        binary_equiv = binary_equiv + '1'  # Adds the number 1 (as a string) to the string for the binary equivalent.
        remaining_value = remaining_value - binary_position_value  # Subtracts the current exponent of 2 from the remaining value.
    else:  # Same indent as the IF statement
        binary_equiv = binary_equiv + '0'  # Adds the number 0 (as a string) to the string for the binary equivalent.

print('The binary equivalent is \"' + binary_equiv + '\"')  # Since the variable for the binary equivalent was built digit-by-digit as a string, we can print it as part of this print statement.