# By Taking Factorial by recusive method

def fact(n):
    if(n==0 or n==1):
        return 1;
    else:
        return n * fact(n-1);

n=fact(4);
print(n);


# By Taking Fibonacci byu recursive method

def Fibonacci(n1):
    if n1 <= 0:
        return 0;
    elif n1 == 1:
        return 1;
    else:
        return Fibonacci(n1 - 1) + Fibonacci(n1 - 2);

print(Fibonacci(10));

