# # valid parenthesis

# exp="{([])}"

# is_valid=True
# stack=[]

# for i in exp:
#     if i in '([{':
#         stack.append(i)
#     else:
#         if len(stack)!=0:
#             if (i==')' and stack[-1]=='(') or (i=='}' and stack[-1]=='{') or (i==']' and stack[-1]=='['):
#                 stack.pop()
#             else:
#                 is_valid=False
#                 break
#         else:
#             is_valid=False
#             break
# if len(stack)!=0:
#     is_valid=False

# print(is_valid)


# sorting colors

# colors=[1,0,2,1,0,2]
# low=mid=0
# high=len(colors)-1

# while mid<=high:
#     if colors[mid]==0:
#         colors[mid],colors[low]=colors[low],colors[mid]
#         low+=1
#         mid+=1
#     elif colors[mid]==1:
#         mid+=1
#     else:
#         colors[high],colors[mid]=colors[mid],colors[high]
#         high-=1
# print(colors)


s="fourtwosevensix"
dici={
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9'
}
# sub=""
# num=""
# for i in s:
#     sub+=i
#     if sub in dici:
#         num=num+dici[sub]
#         sub=""
# print(num)
i=0
j=1
num=0
while j<=len(s):
    if s[i:j] in dici:
        num=num*10+int(dici[s[i:j]])
        i=j
    else:
        j+=1
print(num)

    

