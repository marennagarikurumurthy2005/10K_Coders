amount=5720
dici={}
while amount>0:
    if amount>=1000:
        reminder=amount%1000
        need=(amount-reminder)/1000
        amount=reminder
        dici["1000's"]=int(need)
    elif amount>=500 and amount<1000:
        reminder=amount%500
        need=(amount-reminder)/500
        amount=reminder
        dici["500's"]=int(need)
    else:
        dici["remaining"]=amount
        amount=0


print(dici)