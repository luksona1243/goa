#5) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, შეამოწმეთ 
# რიცხვი ლუწია თუ კენტი და თუ კენტია დაამატეთ ახალ ლისტში 
num = [1,2,3,4,5,6,7,8,9,10]
kenti = []
for i in num:
    if i % 2 != 0:
        kenti.append(i)
print(kenti)