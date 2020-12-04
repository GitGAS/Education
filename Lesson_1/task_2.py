
user_sec = int(input("Введите секуны: "))
hours = user_sec // 60**2
minutes = (user_sec % 60**2) // 60
seconds = (user_sec % 60**2) % 60

print(f"{hours}: {minutes}: {seconds}")
