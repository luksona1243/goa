#3) შექმენით ლისტი სადაც გექნებათ 1-10 ჩათვლით რიცხვები, დაპრინტეთ ყველა რიცხვი 
# მაგრამ მიუწერეთ რომელია კენტი და რომელია ლუწი
num = [1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i % 2 == 0:
        print(f"{i} - ლუწია")
    else:
        print(f"{i} - კენტია")