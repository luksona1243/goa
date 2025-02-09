#7) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიცხვს შემდეგ კი დაბეჭდავს ეს რიცხვი ლუწია თუ კენტი
def num():
    num1 = int(input("sheikvanet ricxvi :"))
    if num1 % 2 == 0:
        print("luwia")
    else:
        print("kentia")
num()