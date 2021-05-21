nums = [5, 4, 88, 3, 2, 121, 9, 21, 8, 7, 6]
print("Sıralama öncesi: ",nums)


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
    return arr


def bubble_sort(arr):
    iteration_count = 0
    for i in range(len(arr)):
        swapped = False
        for index in range(len(arr) - i - 1):
            iteration_count += 1
            if arr[index] > arr[index + 1]:
                arr = swap(arr, index, index + 1)
                swapped = True
        if not swapped:
            return arr


print("Sıralama sonrası: ",bubble_sort(nums)
)

