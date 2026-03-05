# countdown function

def count(n):
    if (n == 0):
        return
    print(n, end="")
    return count(n-1)

count(5)
