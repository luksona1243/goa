#2) ნასწავლ მეთოდებზე შეასრულეთ 3-3 მაგალითი: lower, upper, capitalize, find, len, append, insert, pop
#lower
print("LUKA".lower())           
print("GIGO".lower())  
print("ALAMANTERA".lower())         
print(" ")

#upper
print("luka".upper())           
print("gigo".upper())       
print("alamantera".upper())  
print(" ")


#capitalize
print("luka".capitalize())    
print("gigo".capitalize())         
print("alamantera".capitalize())       
print(" ")

#find
print("luka".find("a"))           
print("gigo".find("g"))         
print("alamantera".find("p"))          
print(" ")

#len
print(len("luka"))                
print(len("gigo"))           
print(len((1,2,3,4,5,6,7)))               
print(" ")

#append
my_list = [1, 2]
my_list.append(3)
print(my_list)                     

fruits = ["luka"]
fruits.append("nika")
print(fruits)                      

nums = []
nums.append(10)
print(nums)                        
print(" ")

#insert
my_list = [1, 3]
my_list.insert(1, 2)
print(my_list)                     

chars = ['a', 'c']
chars.insert(1, 'b')
print(chars)                       

nums = [0, 2]
nums.insert(0, -1)
print(nums)                        
print(" ")

#pop
my_list = [1, 2, 3]
print(my_list.pop())             
                  

letters = ['a', 'b', 'c']
print(letters.pop(0))            
                 

nums = [10, 20, 30]
nums.pop(1)
print(nums)                      
