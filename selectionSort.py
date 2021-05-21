nums = [5, 75, 2, 44, 88, 3, 1]
print("Sıralama öncesi: {0}".format(nums))


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
    return arr


def selection(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            swap(arr, j, j+1)
            j -= 1
    return arr


print('Sıralama Sonrası:', selection(nums))
