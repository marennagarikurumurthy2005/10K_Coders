dici={1:{"username":"mk@2005","password":"mk@2005","otp":1234,"amount":40000}}


while True:
    name=input("username")
    password=input("password")
    otp=int(input("otp"))
    user={"username":name,"password":password,"otp":otp}
    for i in dici:
        extra=dici[i]
        print(extra)
        if name == extra["username"] and password == extra["password"] and otp == extra["otp"]:
            print("Your balance", extra["amount"])
            avail_bal=extra["amount"]
            debit=int(input("Enter amount to debit"))
            if debit>=avail_bal:
                print("Insufficient bal")
            else:
                net=dici[i]["amount"]=avail_bal-debit
                print("debit success")
                print("current",net)
            exit()
        else:
            print("invalide credits")


            exit()

            
    
#     



# data=input()
# sac=ord(data)
# print(sac)

# if ord(data)>=65 and ord(data)<=90:
#     print("caps")
# elif ord(data)>=90 and ord(data)<=122:
#     print("smalls")
# elif ord(data)>=48 and ord(data)<=57:
#     print("digits")
# else:
#     print("special chars")



# if ord(data)%2==0:
#     print("even")
# else:
#     print("odd")



# last_digit=sac%10
# print(last_digit)

# if last_digit%2==0:
#     print("even")
# else:
#     print("odd")


# if last_digit>5:
#     print("Greater")
# else:
#     print("NO")



# inp=int(input())
# char=chr(inp)
# print(char)







        






        


