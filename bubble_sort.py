size=int(input("Enter the size of your array : "))
array=[]
for i in range(size):
    element=int(input("Enter the element you want to enter in your array : "))
    array.append(element)
print("Array before Sorting : ")
for i in range(size):
    print(array[i],end=" ")

for i in range(size-1):
    for j in range(size-i-1):
        if (array[j]>array[j+1]):
            array[j],array[j+1]=array[j+1],array[j]
print("\nArray after sorting : ")
for i in range(size):
    print(array[i],end=" ")