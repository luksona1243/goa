#1 ) მომხმარებელს შემოატაინეთ ორი რიცხვი და მათზე მოახდინეთ მათემატიკური ოპერაციები.
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "გამყოფი ვერ იქნება ნული"
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
