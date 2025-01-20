def is_prime(n):
    if n<=1:
        return False
    elif n ==2:
        return True
    elif n%2 ==0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i ==0:
            return False
    return True
num = int(input("Enter a number to check if it is prime : "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number. ")