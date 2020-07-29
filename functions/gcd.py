
def gcd(number1: int, number2: int) -> int:
    while True:
        big = max(number1, number2)
        small = min(number1, number2)
        remainder = big % small
        if remainder == 0:
            return small
        else:
            number1 = remainder
            number2 = small