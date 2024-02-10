#input: arr[] = {2,6,9}
#output Max = 9
#output Min = 2

arr = [1,5,9,7,3,1]

#finding Maximum value in array
maxarr = arr[0]

for i in range(1,len(arr)):
    if arr[i] > maxarr:
        maxarr = arr[i]    
print(f"Maximum value in a array is : {maxarr}")

#Finding minimum value in array
minarr = arr[0]

for i in range(1,len(arr)):
    if arr[i] < minarr:
        minarr = arr[i]   
print(f"Manimum value in a array is : {minarr}")