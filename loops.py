#num = int(input("Enter a number: "))
#num2 = 1

#while num2 <= 10:
#    print(num, "x", num2, "=", num2 * num)
#    num2 += 1
#while num <= 10:
#    print(num, "x", num2, "=", num2 * num)
#    num += 1

#secret = "password123"
#while secret == "password123":
  #  guess = input("Enter the password: ")
   # if guess == secret:
    #    print("access granted")
    #else:
     #   print("access denied")

#dict = {
#   "table" : ("a piece of furniture", "list of facts & figures"),
#    "cat" : "a small animal"
#}
#print(dict)

#subjects = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
#print(len(subjects))


#num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#for el in num:
#    print(el)

#num = [1,4, 9, 16, 25, 36, 49, 64, 81, 100]
#x = 3
#idx = 0
#for el in num:
#    if (el == x):
#        print("number found at idx", idx)
#        break
#   idx += 1

#for i in range(1, 101, 1):
#    print(i)

#for i in range(101, 0, -1):
#    print(i)

#num = int(input("Enter a number: "))
#for i in range(1, 11, 1):
#    print(num, "x", i, "=", num * i)

#n = 10

#sum = 0
#for i in range(1, 11):
#    sum += i
#print(sum)


#num = int(input("enter a number: "))
#total = num 

#if num == 0:
#        print("the total is", total)
#elif num != 0:
#        total += num
#        num = int(input("enter a number: "))


#def avg(a, b, c):
#     avg = (a + b + c) / 3
#     return (avg)

# print(avg(98, 97, 95))

# friends = ["soumya", "akashat", "ved", "priyansh"]

# def print_len(list):
#     print(len(list))

# print_len(friends)

# friends = ["soumya", "akashat", "ved", "priyansh"]

# def print_el(friends, end = "\n"):
#     print(friends)
#     return friends

# print_el(friends)


# def odd_even(num):
#         if num % 2 == 0:
#                 print(num, "is an even number")
#         else:
#                 print(num, "is an odd number")

#         return num

# odd_even(66)


# File input/output 

# f = open("demo.txt", "r")
# f.write("this is a test file for file handling in pytho")
# f.close()

# f = open("demo.txt", "r")
# print(f.read())


# f = open("demo.txt", "r")
# line2 = f.readline()
# print(line2)
# f.close()
 

# f = open("sample.txt", "w")
# f.write("this is again a sample file created to creat a file inside the code ")
# f.close()

# f = open("sample.txt", "r")
# print(f.read())
# f.close()

# import os
# os.remove("sample.txt")


# f = open("practice.txt", "w")
# f.write(" hi everyone \n we are learning file i/o \n using python. \n i like programming in java \n ")
# f.close()

# f = open("practice.txt", "r")
# print(f.read())
# f.close()

# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "python")
# print(new_data)

# word = "leaning"
# with open("practice.txt", "r") as f:
#     data = f.read()
#     if (data.find(word) != -1):
#         print("found")
#     else:
#         print("not found")

# def word_hunting():
#     word = "learning"
#     with open("practice.txt", "r") as f:
#        data = f.read()
#        if (data.find(word) != -1):
#          print("found")
#        else:
#          print("not found")

# word_hunting()

# class student:
    
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in database...")

        
# class student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("adding new student in database...")

# s1 = student("karan")
# print(s1.name)

# class automotive:

#     brand_name = "bugatti"
#     def __init__(self, name, year):
#         self.model = name
#         self.year = year
#         print("the models are: ")

# s1 = automotive("turbillion", 2026)
# print(s1.model, s1.year)

# s2 = automotive("veron", 2016)
# print(s2.model, s2.year)


# s3 = automotive("chiron", 2020)
# print(s3.model, s3.year)


# s4 = automotive("chiron persport", 2023)
# print(s4.model, s4.year)


# print(s1.brand_name, s1.brand_year)

# print(s2.brand_name, s2.brand_year)

# print(s3.brand_name, s3.brand_year)

# print(s4.brand_name, s4.brand_year)

# name = input("enter your name: ")
# print(name)
# class student:
#     def __init__(self, math, phys, chem):
#         self.math = math
#         self.phys = phys
#         self.chem = chem
 
# s1 = student(88, 78, 86)
# print(s1.math, s1.phys, s1.chem)

# def __init__(self, avg):
#     self.avg = avg

# avg = student((s1.math + s1.phys + s1.chem)/3)
# print(avg)


class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("the total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was debited")
        print("the total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(50000, 12345)
acc1.credit(32000)
acc1.debit(50000)
