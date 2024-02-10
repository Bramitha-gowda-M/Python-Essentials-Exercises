list = [0,5,6,32,4,8,9,2,3,4]

print(list)

#Case 1 : without using inbuild method
count = 0

for i in list:
    count=count+1
print(f"Length of list {list} is {count}")



#using inbuild methond Len()
print(f"Length of a list using len method is {len(list)}")