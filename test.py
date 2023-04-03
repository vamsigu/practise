#print('Hello world')

#a= int(input('enter a number: '))
#b= int(input('enter another number: '))
#sum = a+b
#print(sum)

#import math
#a= int(input('enter a number: '))
#b = int(math.sqrt(a))
#print(b)

# a= float(input('enter a number: '))
# b = a ** 0.5
# print(b)

# a= float(input('enter first side: '))
# b= float(input('enter second side: '))
# c= float(input('enter third side: '))
# s= (a +b +c)/2
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print(area)

# Solve the quadratic equation ax**2 + bx + c = 0
# import cmath
# a= float(input('enter first varible: '))
# b= float(input('enter second variable: '))
# c= float(input('enter third variable: '))
# d = b**2 - (4*a*c)
# sol1 = (-b - cmath.sqrt(d))/ (2*a)
# sol2 = (-b + cmath.sqrt(d))/ (2*a)
# print(f"The two solution of the quadratic equation are {sol1} and {sol2}")

# a= int(input('enter a number: '))
# b= int(input('enter another number: '))
# c = a
# a = b
# b = c
# print(f"value of a is {a} and value of b is {b}")

# import random
# list1 = [0, 1, 2, 3, 4, 5, 6 ,7, 8, 9]
# a = random.choice(list1)
# print(a)

# import random
# a  = random.randint(0, 9)
# print(a)

# km = float(input('enter kilometers: '))
# miles = km*0.621371
# print(miles)

# celsious = float(input('enter celsious value: '))
# F = (celsious*1.8) + 32
# print(F)

# print("Python", end=" ")
# print("is easy to learn.")

# a = float(input('enter a number: '))
# if a == 0:
#     print('number is equal to 0')
# elif a < 0:
#     print('It is a negative number')
# elif a >0:
#     print('It is a positive number')
# else:
#     print('enter a valid number')

# string1 = input('enter a string: ')
# string2 = string1[:: -1]
# if string1 == string2:
#     print('it is a palindrome number')
# else:
#     print('it is not a palindrome number')

# a = int(input('enter a number: '))
# if a%2 == 0:
#     print('it is a even number')
# else:
#     print('it is a odd number')

# a= int(input('enter a number: '))
# b= int(input('enter another number: '))
# c= int(input('enter third number: '))
# d= max(a, b, c)
# print(d)

# year = int(input('enter a year: '))
# if year %4 ==0:
#     print('it is a leap year')
# else:
#     print('it is not a leap year')

# a = int(input('enter a number: '))
# list1 =[]
# for i in range(1, (a+1)):
#     if (a % i) == 0:
#         list1.append(i)
# if len(list1) == 2:
#     print('it is prime number')
# else:
#     print('it is not a prime number')

# num = int(input('enter a number: '))
# p = str(num)
# k = len(p)
# i= 0
# for a in p:
#     i += (int(a) ** k)
# print(i)
# if int(i) == num:
#     print('it is a amstrong number')
# else:
#     print('it is not a amstrong number')

# list1=[]
# for num in range(100, 2001):
#     p = str(num)
#     k = len(p)
#     i= 0
#     for a in p:
#        i += (int(a) ** k)
#     if int(i) == num:
#        list1.append(num)
#     else:
#        continue
# print(list1)

# n = int(input('enter no of natural numbers: '))
# p = (n * (n+1))/2
# print(p)

# n = int(input('enter no of natural numbers: '))
# if n < 0:
#     print('enter a valid number')
# else:
#     sum = 0
#     for i in range(1, (n+1)):
#        sum += i
#     print(sum)

# num = int(input('enter a number: '))
# for i in range(1, (num+1)):
#     p = num*i
#     print(f"{num} x {i} = {p}")

# num = int(input('enter a number:'))
# p = str(num)
# k = p[::-1]
# print(int(k))

# n = int(input('no of lines: '))
# for i in range(1, (n+1)):
#     for j in range(i):
#         print('*', end=" ")
#     print("\n")

# n = int(input('no of lines: '))
# for i in range(1, (n+1)):
#      for j in range(1,(i+1)):
#          print(j, end=" ")
#      print("\n")

# n = int(input('no of lines: '))
# list1 = ['A', 'B', 'C', 'D', 'E','F']
# for i in range(n):
#      for j in range(i+1):
#          print(list1[i], end=" ")
#      print("\n")

# rows = int(input("Enter number of rows: "))
# ascii_value = 65
# for i in range(rows):
#     for j in range(i+1):
#         alphabet = chr(ascii_value)
#         print(alphabet, end=" ")   
#     ascii_value += 1
#     print("\n")

# n = int(input('no of lines: '))
# p = n
# for i in range(1, (n+1)):
#     for j in range(p):
#         print('*', end=" ")
#     p -= 1
#     print("\n")

# n = int(input('no of lines: '))
# p = n
# for i in range(1, (n+1)):
#     for j in range(1, (p+1)):
#         print(j, end=" ")
#     p -= 1
#     print("\n")


# n= int(input('enter no of line: '))
# num = 1
# for i in range(n):
#     for j in range((i+1)):
#         print(num, end=" ")
#         num +=1
#     print('\n')

# num = int(input('enter a number: '))
# exponent = int(input('enter a number: '))
# #a = (num ** exponent)
# a = pow(num, exponent)
# print(a)

# string = input('enter a simple sentence: ')
# if string == string[::-1]:
#     print('it is a palindrome')
# else:
#     print('it is not a palindrome')

# sen1 = input('enter a sentence: ')
# p = sen1.split(" ")
# k = sorted(p)
# for i in k:
#     print(i)

# vowels = "aeiou"
# list1 = []
# sen = input('enter a simple sentence: ')
# for i in vowels:
#     p = sen.count(i)
#     print(f"{i}: {p}")

# string = input('enter a string: ')
# string2 = string.capitalize()
# print(string2)

# num = int(input('enter a number: '))
# p = str(num)
# i = 0
# for k in p:
#     i += 1
# print(i)

# list1= [21, 23, 24, 44, 65]
# for count, i in enumerate(list1):
#     print(count, i)

# my_list = [[1], [2, 3], [4, 5, 6, 7]]
# list1= []
# for i in my_list:
#     for j in i:
#         list1.append(j)
# print(list1)

# list1 = [1, 2, 3]
# list2= [3, 5, 6]
# #list3 = list1 + list2
# list2.extend(list1)
# print(list2)

# list1 = [1, 2, 2, 3 ,4 ,5 ,6 ,7, 8]
# list2= list1[::-1]
# print(list2)

# list1= []
# #if len(list1) == 0:
# if list1 == []:
#     print('list is empty') 

# dict1 = { 'apples': 1, 'banana': 5, 'carrot': 2 }
# list1= sorted(dict1.items(), key = lambda item:item[1])
# dict2 = dict(list1)
# print(dict2)

# dict1 = { 'apples': 1, 'banana': 5, 'carrot': 2 }
# key1 = input('enter a key: ')
# if key1 in dict1.keys():
#     print('this key is present in given dictonary')
# else:
#     print('key is not present in the given dictonary')

# punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# sent= input('enter a sentence with puntuations: ')
# sent1= ''
# for i in sent:
#     if i not in punctuations:
#         sent1 += i
# print(sent1)

# from termcolor import colored
# print(colored('vamsi', 'blue'))

# list1 = [1, 2, 3, 44, 55, 44, 3]
# list2 = []
# for i in list1:
#     if list1.count(i)>=2:
#         list1.remove(i)
# print(list1)
# list2 = list(set(list1))
# print(list2)

# from itertools import permutations
# sent = input('enter a string: ')
# for p in permutations(sent):
#     print("".join(p))

# from itertools import permutations
# string1 = input('enter a string: ')
# string2 = input('enter another string: ')
# if string2 in ["".join(p) for p in permutations(string1)]:
#     print('Two strings are anagram')
# else:
#     print('Two strins are not anagram')

# list1 = ['apples', 'bananas', 'carrot']
# list2 = [1, 4, 2]
# k = zip(list1, list2)
# print(dict(k))  
  
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# k = zip(list1, list2)
# for i, j in k:
#     print(i, j)

# dict1 = { 'apples': 1, 'banana': 5, 'carrot': 2 }
# key = input('enter a key: ')
# if key in dict1.keys():
#     del dict1[key]
# else:
#     print('enter a valid key')
# print(dict1)

# import calendar
# year = int(input('enter a year: '))
# month = int(input('enter a month: '))
# print(calendar.month(year, month))

# def powwer_of_2(k):
#     for i in range((k+1)):
#         p= 2 ** i
#         print(f"2 power {i} is {p}")
# powwer_of_2(10)

# my_list = [12, 65, 54, 39, 102, 339, 221]
# list1 = []
# i = int(input('enter a number: '))
# for k in my_list:
#     if (k % i) ==0:
#         list1.append(k)
# print(list1)

# import math
# a = int(input('enter a number: '))
# b = int(input('enter another number:'))
# c= math.gcd(a, b)
# print(c)

# a = int(input('enter a number: '))
# b = int(input('enter another number:'))
# list1 = []
# if a > b:
#     smaller = b
# else:
#     smaller = a
# for i in range(1, (smaller+1)):
#     if ((a % i) == 0 and (b%i) ==0):
#         list1.append(i)
#     else:
#         continue
# print("the HCF is" +" "+str(max(list1)))

# import math
# a = int(input('enter a number: '))
# b = int(input('enter another number:'))
# c= math.gcd(a, b)
# lcm = (a *b)/c
# print(f"the lcm is {int(lcm)}")

# a = int(input('enter a number: '))
# for i in range(1, (a+1)):
#     if (a % i) ==0:
#         print(i)

# def recur_factorial(n):
#    if n == 0:
#        return 1
#    elif n<0:
#        return "enter a positive value"
#    else:
#        return n*recur_factorial(n-1)
# num = int(input('enter a number: '))
# print(recur_factorial(num))

# def sum(n):
#     if n <= 0:
#         return "enter a positive number"
#     elif n == 1:
#         return 1
#     else:
#         return n + sum((n-1))
# num = int(input('enter no of natural numbers: '))
# print(sum(num))

# def mutiple_func(a, b):
#     return (a+b), (a*b)
# print(mutiple_func(2, 3))

# dec = int(input('enter a decimal number: '))
# p = bin(dec)
# q = oct(dec)
# r = hex(dec)
# print(f"The binary, octal , hexadecimal representations are {p}, {q}, {r}")

# k = input('enter a character: ')
# p = ord(k)
# print(f'The ASIC11 value of {k} is {p}')

# def add(a, b):
#     return a + b
# def sub(a, b):
#     return a - b
# def mul(a, b):
#     return a * b
# def div(a, b):
#     return a/b
# print("1. Addition")
# print("2. subtraction")
# print("3. multiplication")
# print("4. division")
# choice = int(input("enter your choice: "))
# a = int(input('enter a number: '))
# b = int(input('enter another number: '))
# if choice == 1:
#     print(add(a, b))
# elif choice == 2:
#     print(sub(a, b))
# elif choice == 3:
#     print(mul(a, b))
# elif choice ==4:
#     print(div(a, b))
# else:
#     print('enter a valid choice')

# import itertools, random

# deck = list(itertools.product(range(1,14),['Spade', 'Diamond', 'Heart', 'Club']))
# random.shuffle(deck)
# print('you got: ')
# for i in range(5):
#     print(deck[i][0], "of", deck[i][1])

# nterms = int(input('enter a number: '))
# n1 , n2 = 0, 1
# count = 0
# while count < nterms:
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
#     count += 1

# def recur_fibbnoci(n):
#     if n <= 1 :
#         return n
#     else:
#         return (recur_fibbnoci(n-1) + recur_fibbnoci(n-2))
# nterms = int(input('enter a number: '))
# for i in range(nterms):
#     print(recur_fibbnoci(i))

# def recur_bin(n):
#     if n > 1:
#         recur_bin(n//2)
#     print((n%2), end="")
# n = int(input('enter a number: '))
# recur_bin(n)

# def isfloat(string):
#     try:
#         float(string)
#         return True
#     except ValueError:
#         return False
# string = input('enter a string: ')
# print(isfloat(string))

# list1 = [1, 2, 3, 4, 5, 6, 7, 8]
# list2 = []
# i = int(input('enter a number: '))
# for k in range(0, len(list1), i):
#     p = list1[k : (k+i)]
#     list2.append(p)
# print(list2)

# from datetime import datetime
# mystring = "Mar 11 2011 11:31AM"
# required = datetime.strptime(mystring, "%b %d %Y %I:%M%p")
# print(required)

# print('''my name is vamsi
# my surname is G''')

# from shutil import copyfile
# copyfile("./a.text", "./b.text")

# with open('./a.text', 'a') as f:
#     f.write('\nmy surname is gude')

# with open('./a.text', 'r') as f:
#     p = f.read()
#     print(p)

# with open('./a.text', 'r') as f:
#     p = f.readlines()
#     print(p)


# with open('./b.text', 'w') as f:
#     f.write('hello vamsi')

# from datetime import datetime,date,time
# p = datetime.now()
# print(p.year)
# d = p.strftime("%d/%m/%Y, %H:%M:%S")
# d1 =p.strftime("%d %b")
# q = date.today()
# r = q.strftime("%m/%d/%Y")

# list1 = [1, 2, 3, 4, 5, 6]
# for i in range(0,6,2):
#     a = list1[i]
#     list1[i] = list1[i+1]
#     list1[i+1]=a
# print(list1)


# list1 = [1,2,1,1,3,4,4,4,6,8,9,9,9,5,9]
# list2 =[]
# p = tuple(set(list1))
# for i in p:
#     k = list1.count(i)
#     list2.append(k)
# k = zip(p, list2)
# r= dict(k)
# for key in r.keys():
#     if r[key] == max(r.values()):
#         print(key)
#     else:
#         continue

# num = int(input('enter a number: '))
# fact = 1
# while num >= 1:
#     fact *= num
#     num -= 1
# print(fact)

# import calendar
# year = int(input('enter a year: '))
# month = int(input('enter the month: '))
# print(calendar.month(year, month))

# import math
# a = int(input('entter a number: '))
# b = int(input('entter a number: '))
# c = math.gcd(a,b)
# print(c)

# X = [[2,3,1],[5,6,4],[3,5,2]]
# Y = [[7,6,3],[2,4,1],[9,2,3]]
# R = [[0,0,0],[0,0,0],[0,0,0]]

# for i in range(len(X)):
#     for j in range(len(X[0])):
#         R[i][j] = X[i][j] + Y[i][j]
# print(R)

# for i in range(len(X)):
#     for j in range(len(Y[0])):
#         for k in range(len(Y)):
#             R[i][j] += X[i][k]*Y[k][j]
# print(R)

# X =[[1,2],[3,5],[6,7],[3,9]]
# R =[[0,0,0,0],[0,0,0,0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         R[j][i] = X[i][j]
# print(R)

# list1=[{"name":"kohir","rollno":36},{"name":"mani","rollno":35},{"name":"kl","rollno":32},{"name":"kl","rollno":30}]
# list2 =[]
# list3= []
# for i in range(len(list1)):
#     p = list1[i]["rollno"]
#     list2.append(p)
# for q in range(len(list2)):
#     for k in range(len(list1)):
#         p1 = min(list2)
#         if list1[k]["rollno"] == p1:
#             list3.append(list1[k])
#             del list1[k]
#             list2.remove(p1)
#         else: 
#             continue
# print(list3)

# a = input('enter a string: ')
# for i in range(0, len(a),2):
#     p = a[i]
#     print(p, end="")
# print(a[0::2])

# string = "abcabc"
# p = list(set(list(string)))
# print(p)
# for i in p:
#     k = string.count(i)
#     print(i,k)

# list1 = [12,24,35,24,88,120,155,88,120,155]
# list2 =[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print(list2)

# n = int(input('enter a number: '))
# sum = 0
# for i in range(1,n+1):
#     sum += i/(i+1)
# print(sum)

# str = input('enter a sentence: ')
# list1 =[]
# list2 = []
# list3 =[]
# for i in str:
#     if i.isupper():
#         list1.append(i)
#     elif i.islower():
#         list2.append(i)
#     else:
#         list3.append(i)
# print(len(list1))
# print(len(list2))
# print(len(list3))


# dict1 ={"apple":3,"banana":8,"carrot":2}
# p =max(dict1.values())
# max2 =0
# for i in dict1.values():
#     if (i>max2 and i<p):
#         max2 = i
# print(max2)

# list1 = [i for i in range(1000,3001)]
# list2 =[]
# list3 =[]
# for i in range(1000,3001):
#     p = str(i)
#     for q in p:
#         if int(q)%2 != 0:
#             list2.append(i)
#         else:
#             continue
# p = list(set(list1)-set(list2))
# print(p)

# n = int(input('enter a number: '))
# for i in range(1,(n+1)):
#     if n%i == 0:
#         if i%2 == 0:
#             print(i," it is a even factor")
#         else:
#             print(i," it is an odd factor")
#     else:
#         continue

# sequence = input('enter sequence of words: ')
# p = sequence.split(",")
# q = sorted(p)
# for i in q:
#     print(i,end=",")

# string = input('entera sentence: ')
# print(string[::-1])

# list1 =[1,3,6,78,35,55]
# list2 =[12,24,35,3,88,120,155]
# list3 =[]
# for i in list1:
#     if i in list2:
#         list3.append(i)
#     else:
#         continue
# print(list3)

# list1 =[12,24,35,24,88,155,120,155,88,120]
# list2 =[]
# for i in list1:
#     if i  not in list2:
#         list2.append(i)
#     else:
#         continue
# print(list2)

# import random
# list1 =[]
# list2 =[]
# for i in range(1,1001):
#     if (i%5 ==0 and i%7 ==0):
#         list1.append(i)
# for i in range(5):
#     p = random.choice(list1)
#     list2.append(p)
# print(list2)

# list1 = [12,24,35,24,88,120,155]
# list2 =[i for i in list1 if i!=24]
# print(list2)

# list1 = [12,24,35,70,88,120,155]
# list2 =[list1[i] for i in range(len(list1)) if i not in (0,4,5)]
# print(list2)

# list1 = [12,24,35,70,88,120,155]
# list2 = [i for i in list1 if not(i%5==0 and i%7==0)]
# print(list2)

# def factorial(n):
#     if n ==0 or n==1:
#        return 1
#     elif n>1:
#       return n*factorial(n-1)
#     else:
#        return "Invalid nummber"
    
# p = factorial(5)
# print(p)

# a = int(input('enter a number: '))
# b = int(input('enter an another number: '))
# list1 =[]
# for i in range(a):
#     list2 =[]
#     for j in range(b):
#         p = i*j
#         list2.append(p)
#     list1.append(list2)
# print(list1)

# list1 = [i for i in range(2000,3201)]
# list2 = []
# for i in list1:
#     if i%5 != 0 and i%7 == 0:
#         print(i,end=",")

# sentence = input('enter a string: ')
# p = sentence.split(" ")
# list1 =[]
# for i in p:
#     if i not in list1:
#         list1.append(i)
# q = sorted(list1)
# print(" ".join(q))

# import shutil
# shutil.copyfile("./a.text","./test1.txt")
# shutil.move("./test1.txt","./b1.text")

# import os
# os.remove("./b1.text")
# os.rename("./c.text","./c1.text")

# with open("./a.text","r") as f:
#     p = f.readlines()
#     print(p)
#     print(len(p)) 

# list1 = ["hello vamsi\n","my native place is kanigiri\n","I did my B.Tech in Nit Trichy"]
# with open("./a.text","w") as f:
#     f.writelines(list1)

# with open("./a.text", "a") as f:
#     f.write("\nI am doing job in bangalore")

# import re
# with open("./a.text","r+") as f:
#     a = f.readlines()
#     for i in range(len(a)):
#         b = re.search("bangalore",a[i])
#         if b:
#             print("present in line",(i+1))
#             print(b.span())
#         else:
#             print("not present in line", (i+1))

# import os
# for i in os.listdir("./"):
#     if i.endswith(".txt"):
#         print(i)

# string= input('enter a string: ')
# for i in range(1, len(string),2):
#     for j in range(int(string[i])):
#         print(string[i-1],end="")

# def decimal(n):
#     sum = 0
#     for i in range(len(n)):
#         sum += (int(n[len(n)-1-i])*pow(2,i))
#     return sum
# s = input('enter the sequence: ')
# p = s.split(',')
# for i in p:
#     if decimal(i)%5 == 0:
#         print(i,end=",")

# l = ["apple","banana"]
# for i in l:
#     for k in i:
#         print(k,(ord(k)-96))

# a = int(input('total vehicles: '))
# b = int(input('total tyres: '))
# for i in range(1,(a+1)):
#     if (2*i)+((a-i)*4) == b:
#         print('two wheelers',':',i)
#         print('four wheelers',":",(a-i))

# l = [7,4,8,2,9]
# count = 0
# for i in range(len(l)):
#     if i == 0:
#         count += 1
#     else:
#         if l[i] > max(l[0:i]):
#             count +=1
# print(count)
