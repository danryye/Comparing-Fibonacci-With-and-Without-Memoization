import time

# Program Settings
N = 42 # Population Size - value size being calculated

def check_input(N: int): # Checks N to be a positive integer value
    if type(N) != int:
        raise TypeError("The input N must be a positive integer.")
    if N < 1:
        raise ValueError("The input N must be a positive integer.")

print(f"Starting calculations on fibonacci at {N}")
########################################
###### Fibonacci Without Caching #######
########################################
operation_name = "Fibonacci Without Caching"
fib_st = time.perf_counter() # Start time of operation
def fibonacci(n: int):
    check_input(N) # Checks for valid input

    # Calculations for fibonacci of n
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Outputs Results
fib_result = fibonacci(N)
fib_td = time.perf_counter() - fib_st # Calculates time delta
print(f"{operation_name} completed with the result {fib_result}")
print(f"It took {fib_td*1E3:.2f} ms/{fib_td:.1f} s to complete")

########################################
####### Fibonacci With Caching #########
########################################
operation_name = "Fibonacci With Caching"
cached_fib_st = time.perf_counter() # Start time of operation

# Dictionary to store fibonacci results to reduce calculations needed.
fibonacci_cache = {}

def fibonacci_with_cache(n: int):
    check_input(N) # Checks for valid input

    # if n was already calculated before, skips calculation and returns the value.
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Calculations for fibonacci of n
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_with_cache(n - 1) + fibonacci_with_cache(n - 2)

    # Adds the value to the cache and returns it
    fibonacci_cache[n] = value
    return value

# Outputs Results
cached_fib_result = fibonacci_with_cache(N)
cached_fib_td = time.perf_counter() - cached_fib_st # Calculates time delta
print(f"{operation_name} completed with the result {cached_fib_result}")
print(f"It took {cached_fib_td*1E3:.2f} ms/{cached_fib_td:.1f} s to complete")

# Overall Results
print()
print(f"In this test, Fibonacci Without Caching took {fib_td*1E3:.2f} ms/{fib_td:.1f} s to complete")
print(f"In this test, Fibonacci With Caching took {cached_fib_td*1E3:.2f} ms/{cached_fib_td:.1f} s to complete")
print(f"The operation with caching was faster than the operation without caching by {fib_td - cached_fib_td} s")
