def fibonacci():
    num = int(input("Enter the sequence numbers"))
    i = 1
    a=1
    b=1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [a]
    elif num == 2:
        fib = [a,b]
    elif num > 2:
        fib = [a,b]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
input()
