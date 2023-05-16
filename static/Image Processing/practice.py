
# def func(a, *args, **kwargs):
#     print("These Are the Keys")
#     for a,b in a.items():
#         if b=="":
#             continue
#         print(a,b)
#     print()
#     for i in args:
#         print(i)
#     print()
#     for i,j in kwargs.items():
#         print(i,j)
#
#
# a={"Saim":"CR","Uzair":"Head Boy","Abd":"Cheater","Zain":"Funny","Amir":"Player","Zarwa":"Topper"}
# b=["Saim","Uzair","Zarwa","Zain","Amir"]
# c={"CR" :"aa","Head Boy":"","Funny":"","Player":"","Topper":""}
# func(a,*b,**c)


"""------------------------------------Time Module (asc time)-----------------------------

import time

def abc(b):
    a={}
    for i in range(6):
        if i==0:
            a[b[i]]="Year"
        elif i==1:
            if b[i]==1:
                a["January"] = "Month"
            elif b[i]==2:
                a["Feburary"] = "Month"
            elif b[i]==3:
                a["March"] = "Month"
            elif b[i]==4:
                a["April"] = "Month"
            elif b[i]==5:
                a["May"] = "Month"
            elif b[i]==6:
                a["June"] = "Month"
            elif b[i]==7:
                a["July"] = "Month"
            elif b[i]==8:
                a["August"] = "Month"
            elif b[i]==9:
                a["September"] = "Month"
            elif b[i]==10:
                a["October"] = "Month"
            elif b[i]==11:
                a["November"] = "Month"
            elif b[i]==12:
                a["December"] = "Month"
        elif i==2:
            a[b[i]]="Day"
        elif i==3:
            a[b[i]]="Hour"
        elif i==4:
            a[b[i]]="Min"
        elif i==5:
            a[b[i]]="Sec"
    for i,j in a.items():
            print(f"{j} = {i}.")

# a=time.time()
b=time.localtime(time.time())
x=abc(b)
# print(x)               """


# import time
# # print(time.asctime(time.localtime(time.time())))
# a=time.time()
# for i in range(4):
#     print("I love Saim")
#     time.sleep(2)
# print(float(time.time()-a))

"""---------------------------------Enumerate Function------------------------------------------"""
# import time
# l1=["Palak","Cucumber","Lemon","Bhindi","Aloo","Podina","Dhania"]
# initial1=time.time()
# for i, j in enumerate(l1):             #Here i =Index AND j =item
#     if i%2==0:
#         print(j)
# print(f"TIme Required for Enumerate in {time.time()-initial1}")

"""-------------------------------How does Import Statement Work----------------------------------------"""
# for i in range (5):
#     a=2
#     f=lambda i,a:i+a
#     print(f(i,a))

"""----------------------------------------Filter Function-----------------------------------------------"""
# l=[1,2,3,4,5,6,7,8,9]
# x=list(filter(lambda num:num>5,l))        #here Filter Function Allows Trues to pass and Falses are filtered
# print(x)

"""----------------------------------------Map Function-----------------------------------------------"""
# l = [6,1, 2, 3, 4, 5]
# f=list(map(lambda x:str(x),l))
# print(f)
# print(type(f[3]))
#
"""----------------------------------------Reduce Function-----------------------------------------------"""
# from functools import reduce
# l = [1, 2, 3, 4, 5]
# t=reduce(lambda x,y: x+y,l)
# print(t)

"""--------------------------------------practice snake water Gun-----------------------------------------"""
# import random
# l=["Saim","Zarwa","Yahya"]
# x=random.choice(l)
# print(x)

#Water ---------------------- 200ml glass ----------------- Any distrib B/W 9am - 5pm------------3.5 litres
#Eyes ----------------------- Every 30 mins
#Physical ------------------- Every 45 mins
#Record in a file-----
#Rules
# Use pygame module to play Audio
# file="Water.mp3"
# pygame.init()
# mixer.music.load(file)
# mixer.music.play()
# time.sleep(2)
# print("ok")

# import time
# from pygame import mixer
# water="Water.mp3"
# Eyes="Exercise.mp3"
# Exercise="Eyes.mp3"
# pygame.init()
# ini1=time.time()
# ini2=time.time()
# ini3=time.time()
# while True:
#     #For Water
#     if time.time()-ini1>1645.2 and time.time()-ini1<1646 :
#         # mixer.music.load(water)
#         # mixer.music.play()
#         # time.sleep(2)
#         ini1 = time.time()
#         print("Water")
#         a = input("Press any key to Stop:")
#         with open("E:\\Eyes.txt","a") as f:
#             x=f.write(f"Water drunk done at {time.asctime(time.localtime())}")
#     #For Eyes
#     elif time.time()-ini2>1800 and time.time()-ini2<1802 :
#         # mixer.music.load(water)
#         # mixer.music.play()
#         # time.sleep(2)
#         ini2=time.time()
#         print("Phy")
#         a=input("Press any key to Stop:")
#         with open("E:\\Eyes.txt","a") as f:
#             y=f.write(f"Physical Exercise done at {time.asctime(time.localtime())}")
#     # For Exercise
#     elif time.time()-ini3>2700 and time.time()-ini3<2702 :
#         # mixer.music.load(water)
#         # mixer.music.play()
#         # time.sleep(2)
#         ini3=time.time()
#         print("Eyes")
#         a=input("Press any key to Stop:")
#         with open("E:\\Eyes.txt","a") as f:
#             z=f.write(f"Eyes Exercise done at {time.asctime(time.localtime())}")




# def cond(a):
#     def case1():
#         print("1")
#
#     def case0():
#         print("0")
#
#     if a==0:
#         del case1
#     elif a==1 :
#         del case0
#     try :
#         case1()
#     except :
#         return case0()
#     # try :
#     #     case0()
#     # except Exception as e:
#     #     print(e)
#
# cond(0)

# try :
#     print(2+2)
# finally:
#     print(0)
# f= open("C:\\Users\\saimy\\Desktop\\aaa.txt","rb")
# print(type(f.read()))
# q= open("C:\\Users\\saimy\\Desktop\\aaa.bmp","wb")
# q.write(binary)
from Tools import Edit_tools
def january():
    return "January"

def february():
    return "February"

def march(a,b):
    return "march"

def april():
    return "April"

def may():
    return "may"

def june():
    return "June"

def july():
    return "July"

def august():
    return "august"

def september():
    return "September"

def october():
    return "October"

def november():
    return "I am November"

def december():
    return "December"

def default():
    return "Incorrect Month"


p=Edit_tools()
inp=open("C:\\Users\\saimy\\Desktop\\sample22.bmp","rb")
out=open("C:\\Users\\saimy\\Desktop\\sampleCopy.bmp","r+b")
switcher = {

    0: january(),

    "gray": p.grayScale,

    2: march,

    3: april()

}

# print(switcher.get("gray",default())(inp,out))
print(switcher.get("gray",default())(inp,out))
# def month(monthOfYear):
#     a=switcher.get(monthOfYear, default)
#     return a()

# print(month(1))

# print(month(0))





