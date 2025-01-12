def is_prime(number):
    flag = True
    if number <= 1:
        flag = False
        return flag
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            flag = False
            break
    return flag

print(is_prime(2))