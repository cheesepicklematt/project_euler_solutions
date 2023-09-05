
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    
    # Check if the number is divisible by 2 or 3
    if number % 2 == 0 or number % 3 == 0:
        return False

    # Only need to check divisors up to sqrt(number)
    # Any number greater than the square root that divides the number
    # will have a corresponding divisor smaller than the square root.
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

checkList = [x for x in range(1,1_000_000,2) if x%5!=0]
count = 2 # for 3 and 5
for n in checkList:
    if is_prime(n):
        count += 1
        if count == 10001:
            break

print(n)
