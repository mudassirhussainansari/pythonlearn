#factorial function in python 

value = int(input("Enter the value do you need for factorial: "))

def fact_fun(n):
    fact = 1
    for i in range (1, n+1):
        fact = fact * i
    return fact

# factorial = fact_fun(value)

print(fact_fun(value))
