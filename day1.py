def square(n):
    return n*n
def is_even(n):
    return n%2==0
def max_of_three(num1, num2, num3):
    if(num1>num2 and num1>num3 ):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3
def greetuser(name,greeting="hello"):
    return f"{greeting} {name}!"

print(square(65))
print(is_even(68))
print(max_of_three(88,76,9))
print(greetuser("Asiya"))
print(greetuser("Asiya","hi"))


