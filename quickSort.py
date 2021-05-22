from random import randrange, shuffle


def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
    # return arr


def quick_sort(arr, start, end):
    # Base case: Array'de 1 veya 0 eleman kaldıysa bitir.
    if start >= end:
        return arr
    # Pivot seçme işlemi. Algoritma verimliliğini sağlayabilmek için rastgele seçiyoruz.
    pivot_index = randrange(start, end + 1)
    pivot_element = arr[pivot_index]

    # Pivotu sona alıyoruz.
    swap(arr, pivot_index, end)
    # Liste
    start_pointer = start
    for i in range(start, end):
        if arr[i] < pivot_element:
            swap(arr, i, start_pointer)
            start_pointer += 1
    # Start pointer ile son eleman(pivot) yer değiştirdi. Artık merkezde pivot var
    swap(arr, start_pointer, end)
    # Array 2'ye bölündü
    quick_sort(arr, start, start_pointer-1)  # Pivottan öncesi sola ayrıldı.
    quick_sort(arr, start_pointer + 1, end)  # Pivottan sonrası sağa ayrıldı.


arr = [5, 4, 88, 3, 2, 121, 9, 21, 8, 7, 6]
shuffle(arr)
print("Sıralama öncesi: ", arr)
quick_sort(arr, 0, len(arr)-1)
print("Sıralama sonrası: ", arr)
