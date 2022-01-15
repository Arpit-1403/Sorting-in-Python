size=int(input("Enter the size of your array : "))
array=[]
for i in range(size):
    element=int(input("Enter the element you want to enter in your array : "))
    array.append(element)
print("Array before Sorting : ")
for i in range(size):
    print(array[i],end=" ")
i=0
for i in range(size):
    min=i
    for j in range(i+1,size):
        if(array[j]<array[min]):
            min=j

    if(i!=min):
        array[i],array[min]=array[min],array[i]

print("\nArray after sorting : ")
i=0
for i in range(size):
    print(array[i],end=" ")
