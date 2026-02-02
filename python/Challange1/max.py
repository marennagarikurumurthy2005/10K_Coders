# Problem 1
#  def find_one()



# Problem 3
def max_find(employess):

    summuation=0
    
    for i in employess:
        summuation=summuation+employess[i]
        # maxi=max(maxi,employess[i])
    n=len(employess)

    average=summuation/n
    dici={}
    for j in employess:
        if employess[j]>average:
            dici[j]=employess[j]
    return dici
            
employes={
    "A":3000,
    "B":4000,
    "C":5000,
    "x":4000,
    "j":1000
    
}
result=max_find(employes)
print(result)






# Problem 2



""" def Validate(email):
    special_char=0
    char=0
    atemail=0
    extension=""
    domain=""


    


    




email=user@gmail.com
result(Validate(email)) """
