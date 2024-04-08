"""
PowerOfTen
"""
# Provide your solution here
number = int(input("Enter a max 3-digit number: "))
if number < 0:
    print("Number cannot be negative!")
elif number > 999:
    print("Number has more than 3 digits!")
else:
    result0 = number // 100
    result1 = number // 10
    result2 = number % 10
    print(f"{number} = {result0} * 100 + {result1} * 10 + 1 * {result2}")

"""
Cash Box
"""
# Provide your solution here
pay_sum = int(input("To pay: "))
received = int(input("Received: "))
while True:
    if pay_sum > 0:
        if pay_sum - received > 0:
            print(f"Your change is: {pay_sum - received}")
            break
        elif pay_sum - received == 0:
            print("Thank you!")
            break
        else:
            print("You did not pay enough!")
    else:
        print("Negative payment is invalid!")
        continue
