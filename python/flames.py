# name1=input("Enter your name:").upper()
# # print(name1)
# name2=input("Enter your LOVE's name:").upper()
# slamletters=""

# for i in name1:
#     if i not in name2:
#         slamletters+=i
# for j in name2:
#     if j not in name1:
#         slamletters+=j
    
# slam_without_dublicates=""
# for i in slamletters:
#     if i not in slam_without_dublicates:
#         slam_without_dublicates+=i


# slam_list=['F','L','A','M','E','S']

# while len(slam_list)>1:
#     num=len(slam_without_dublicates)
#     while num>len(slam_list):
#         num=num-len(slam_list)
#     slam_list.remove(slam_list[num-1])
    
# print(slam_list)


# flames_word_count=6
# letters_length=len(slamletters)

    
# flames={"F":"Friends","L":"Love","A":"Attraction","M":"Marriage","E":"Enemies","S":"Soulmates"}

# print(flames[slam_list[0]])

print("Flames")
while True:
    print()
    data=int(input("Enter 1 to continue:"))
    if data==1:
        name1 = input("Enter your name: ").upper()
        name2 = input("Enter your LOVE's name: ").upper()

        slamletters = ""

        for i in name1:
            if i!=" " and i not in name2:
                slamletters += i

        for j in name2:
            if j!=" " and j not in name1:
                slamletters += j

        slam_without_duplicates = ""

        for i in slamletters:
            if i not in slam_without_duplicates:
                slam_without_duplicates += i

        count = len(slam_without_duplicates)

        flames_list = ['F', 'L', 'A', 'M', 'E', 'S']

        index = 0

        while len(flames_list) > 1:
            index = (index + count - 1) % len(flames_list)
            flames_list.pop(index)

        flames = {
            "F": "Friends",
            "L": "Love",
            "A": "Attraction",
            "M": "Marriage",
            "E": "Enemies (Wife & Husband)",
            "S": "Soulmates"
        }

        # print("Remaining Letter:", flames_list[0])

        print("Relationship:", flames[flames_list[0]])
    
    elif data==2:
        print("You choose exit")
        break
    else:
        print("Invalid input")
        break






