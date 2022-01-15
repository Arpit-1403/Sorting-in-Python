def partition(array,low,high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1

        

def quicksort(array,low,high):
    if low<high:
        pi=partition(array,low,high)
        quicksort(array,low,pi-1)
        quicksort(array,pi+1,high)


size=int(input("Enter the size of your array : "))
array=[]
for i in range(size):
    element=int(input("Enter the element you want to enter in your array : "))
    array.append(element)
print("Array before Sorting : ")
for i in range(size):
    print(array[i],end=" ")
quicksort(array,0,size-1)
print("\nArray after sorting : ")
for i in range(size):
    print(array[i],end=" ")