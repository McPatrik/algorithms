arr = [1,6,8,2,4,90,2,4,9999,0,-1, 66, 77, 56]

# def bubbleSort(array):
#   for i in range(len(array)-1,0,-1):
#     for j in range(i):
#       if array[j] > array[j+1]:
#         array[j],array[j+1] = array[j+1],array[j]
#   return array

# print(bubbleSort(arr))

# def choiceSort(array):
#   sortArr = []
#   for y in range(0,len(array)):
#     minimum = array[0]
#     indexMin = 0
#     for i in range(1,len(array)):
#       if array[i] < minimum:
#         minimum = array[i]
#         indexMin = i
#     array.pop(indexMin)
#     sortArr.append(minimum)
#   return sortArr;
# print(choiceSort(arr))

# print(arr + [7,8])
def quickSort(array):
  if(len(array) < 2):
    return array
  else:
    pivot = array[len(array)//2]
    array.pop(len(array)//2)
    minArr = [i for i in array if i <= pivot]
    maxArr = [i for i in array if i > pivot]
    print(minArr,pivot,maxArr)
    return quickSort(minArr) + [pivot] + quickSort(maxArr)
print(quickSort(arr))
