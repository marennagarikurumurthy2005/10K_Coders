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

colors=[1,0,2,1,0,2]
low=mid=0
high=len(colors)-1

while mid<=high:
    if colors[mid]==0:
        colors[mid],colors[low]=colors[low],colors[mid]
        low+=1
        mid+=1
    elif colors[mid]==1:
        mid+=1
    else:
        colors[high],colors[mid]=colors[mid],colors[high]
        high-=1
print(colors)


# s="fourtwosevensix"