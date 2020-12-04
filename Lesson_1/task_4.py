
user_number = int(input("Введите, пожалуйста, целое положительное число: "))
max_digit = user_number % 10
user_number = user_number // 10
while user_number > 0:
    if user_number % 10 > max_digit:
        max_digit = user_number % 10
    user_number = user_number // 10
print(max_digit)
