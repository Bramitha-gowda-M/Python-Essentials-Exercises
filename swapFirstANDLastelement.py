#case 1 : using temp variable
list = [12,35,62,1,2,3,8,9]
print("Case 1 :")
print(f"List before Swapping{list}")
temp = list[0]
list[0] = list[-1]
list[-1] = temp
print(f"List after Swapping : {list}")


#Case 2 : Extracting the first and last value and interchaging the values of indexes
list1 = [19,3,6,5,4,12,0]
print('\nCase 2 :')
print(f"List before Swapping{list1}")
list1[0],list1[-1] = list1[-1], list1[0]
print(f"List after Swapping : {list1}")


#case 3 : using Tupple variable
list2 = [6,3,2,5,4,1]
print('\nCase 3 :')
print(f"List before Swapping{list2}")
get = (list2[-1],list2[0]) #packing
list2[0],list2[-1] = get #unpacking
print(f"List after Swapping : {list2}")


#Case 4 : using * opperand
list3 = [7,2,3,1,4,5,8]
print('\nCase 4 :')
print(f"List before Swapping{list3}")
start,*middle,end = list3
list3 = [end,*middle,start]
print(f"List after Swapping : {list3}")


#case 4 : Using Pop() build in method
list4 = [6,2,1,4,5]
print('\nCase 5 :')
print(f"List before Swapping{list4}")
first = list4.pop(0)
last = list4.pop(-1)
list4.insert(0,last)
list4.append(first)
print(f"List after Swapping : {list4}")