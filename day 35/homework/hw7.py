#8) შექმენით ფუნქცია რომელიც მომხმარებელს შეეკითხება რიღხვს შემდეგ კი დაბეჭდავს დადებითია თუ უარყოფითი
def num():
    num1 = int(input("sheikvanet ricxvi :"))
    if num1 > 0:
        print("dadebitia")
    elif num1 <0:
        print("uarkofitia")
    else:
        print("tolia 0 is")
num()