from typing import List

def merge_sort(data) -> None:
  if len(myList) > 1:
    mid = len(myList) // 2
    left = myList[:mid]
    right = myList[mid:]

# Recursive call on each half
    merge_sort(left)
    merge_sort(right)

# Two iterators for traversing the two halves
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
      if left[i] <= right[j]:
        myList[k] = left[i]
        i += 1
      else:
        myList[k] = right[j]
        j += 1
      k += 1

# For all the remaining values
while i < len(left):
  myList[k] = left[i]
  i += 1
  k += 1

while j < len(right):
  myList[k]=right[j]
  j += 1
  k += 1


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data)
print(data)
