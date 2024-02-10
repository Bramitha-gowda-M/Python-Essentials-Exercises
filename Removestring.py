list = ['python',"java","c","c++","python"]

word = "python"
n=2 #occurance of the word
count = 0  #counts the word occurance

for i in range(0,len(list)):
    if(list[i]==word):
        count = count +1
        if count == n:
            del list[i]
            
print("The list is : ",list)