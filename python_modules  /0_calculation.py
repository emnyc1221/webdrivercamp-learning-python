#!/usr/bin/python3
if __name__=="__main__":
    from calculation import add, sub, mul, div  # Import specific functions from calculation.py

a = 4  # Use this variable as the first argument to call a function
b = 2  # Use this variable as the second argument to call a function

result_add = add(a, b)
result_sub = sub(a, b)
result_mul = mul(a, b)
result_div = div(a, b)

    # Print the results
print(f"{a} + {b} = {result_add}")
print(f"{a} - {b} = {result_sub}")
print(f"{a} * {b} = {result_mul}")
print(f"{a} / {b} = {result_div}")
