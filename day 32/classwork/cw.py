#    1) შექმენით სია რომელშიც იქნება 10 სხვადასხვა რენდომ რიცხვი, შემდეგ მიწდვით ამ სიის თითოეულ ელემენტს და დაბეჭდეთ თითოეული ელემენტი ოღონდ თუ რიცხვი იქნება ხუთის ჯერადი მიუწერეთ გვერძე რომ ხუთის ჯერადია ხოლო სამის ჯერადებს მიუწერეთ რომ სამის ჯერადია
num = [11,22,12,323,56,23,34,5,2,34,57,10,25,44,67,43]
for numb in num:
    if numb % 5 == 0:
        print(f"{numb} xutis jeradia")
    elif numb % 3 == 0:
        print(f"{numb}samis jeradia")
    else:
        print(numb)
    