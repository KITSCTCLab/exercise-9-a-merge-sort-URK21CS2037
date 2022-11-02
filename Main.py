from typing import List

def merge(array, l, m, r):
    array2 = [0 for i in range(r + 1)]
    i = l
    j = m + 1
    k = l
    while i <= m and j <= r:
        if array[i] <= array[j]:
            array2[k] = array[i]
            i += 1
        else:
            array2[k] = array[j]
            j += 1
        k += 1
    if i > m:
        while j <= r:
            array2[k] = array[j]
            j += 1
            k += 1
    else:
        while i <= m:
            array2[k] = array[i]
            i += 1
            k += 1
    for i in range(l, r + 1):
        array[i] = array2[i]

def merge_sort(array, l, r) -> None:
  # Write code here
  if l < r:
        m = (l + r) // 2
        merge_sort(array, l, m)
        merge_sort(array, m + 1, r)
        merge(array, l, m, r)


# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
merge_sort(data, 0, len(data) - 1)
print(data)
