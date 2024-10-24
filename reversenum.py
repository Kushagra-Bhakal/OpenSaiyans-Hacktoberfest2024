def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10  # Get the last digit
        reversed_num = reversed_num * 10 + digit  # Add it to the reversed number
        n = n // 10  # Remove the last digit from the original number
    return reversed_num

# Example usage
number = int(input("Enter a number: "))
reversed_result = reverse_number(number)
print(f"The reverse of {number} is {reversed_result}.")
