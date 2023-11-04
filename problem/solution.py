


def fib_last_digit(n):
    a = 0
    b = 1
    for i in range(2, n+1):
        c = (a + b) % 10
        a = b
        b = c
    return b
print("Enter the index number : ")
n = int(input())
print(fib_last_digit(n))


# F200 = 280 571 172 992 510 140 037 611 932 413 038 677 189 525