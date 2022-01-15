size=int(input("Enter the size of your array : "))
array=[]
for i in range(size):
    element=int(input("Enter the element you want to enter in your array : "))
    array.append(element)
print("Array before Sorting : ")
for i in range(size):
    print(array[i],end=" ")
for i in range(1,size):
    key=array[i]
    j=i-1
    while j>=0 and key<array[j]:
        array[j+1]=array[j]
        j=j-1
    array[j+1]=key
print("\nArray after sorting : ")
i=0
for i in range(size):
    print(array[i],end=" ")