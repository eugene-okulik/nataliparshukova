import random


def final_salary():
    salary = int(input('input salary: '))
    is_bonus = random.choice([True, False])
    bonus = 0
    if is_bonus:
        bonus = random.randint(100, 10000)
    result = salary + bonus
    print(f"salary={salary}, is_bonus={is_bonus}, bonus={bonus}, final_salary={result}")

final_salary()
