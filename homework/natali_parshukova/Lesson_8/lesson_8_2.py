def fibonacci(position):
    num1 = 0
    num2 = 0
    counter = 0
    while counter < position:
        if counter == 0:
            num1 = 0
            yield 0
        elif counter == 1:
            num2 = 1
            yield 1
        else:
            num_n = num1 + num2
            num1 = num2
            num2 = num_n
            yield num_n
        counter += 1


count = 1
for fibonacci_number in fibonacci(201):
    if count == 5:
        print(f"fibonacci(5): {fibonacci_number}")
    elif count == 15:
        print(f"fibonacci(15): {fibonacci_number}")
    elif count == 50:
        print(f"fibonacci(50): {fibonacci_number}")
    elif count == 100:
        print(f"fibonacci(100): {fibonacci_number}")
    elif count == 200:
        print(f"fibonacci(200): {fibonacci_number}")
    count += 1
