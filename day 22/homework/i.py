# 1) მომხმარებელს შემოატანინეთ რიცხვი შემდეგ კი ერთიდან ამ რიცხვამდე დაბეჭდეთ ყველა რიცხვის ჯამი
number = int(input("sheikvanet ricxvi: "))
total_sum = 0
for i in range(1, number + 1):
    total_sum += i
print({total_sum})