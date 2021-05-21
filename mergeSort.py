def merge_sort(items):
    if len(items) <= 1:
        return items

    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)


def merge(left, right):
    result = []

    while (left and right):
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left
    if right:
        result += right

    return result


liste1 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202,
          534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]

print('Sıralama öncesi: ', liste1)
print('Sıralama sonrası: ', merge_sort(liste1))
