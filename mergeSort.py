def merge_sort(items):
    #Base Case: Array 1 veya 0 elemana sahipse Array'i geri döndürür.
    if len(items) <= 1:
        return items
    #Array'i ortadan 2'ye böler.
    middle = len(items) // 2
    #Array'in sol parçası
    left = items[:middle]
    #Array'in sağ parçası
    right = items[middle:]
    #Yinelemeli bir şekilde sol parçaları daha küçük sol parçalara ayırır. Base Case gerçekleşene kadar !!.
    left_sorted = merge_sort(left)
    #Yinelemeli bir şekilde sağ parçaları daha küçük sağ parçalara ayırır. Base Case gerçekleşene kadar !!.
    right_sorted = merge_sort(right)
    #Ayrılmış ıarçaları birleştiren fonksiyonu çağırır.
    return merge(left_sorted, right_sorted)

#Rekürsif bir şekilde küçük parçalara ayrılan listeyi sıralı bir şekilde tekrar birleştirir.
def merge(left, right):
    #Her birleştirme çağrısından sonra birleştirilen parçaları depolar.
    result = []
    #Sol veya sağ listeden herhangi biri boşalana kadar devam eder.
    while (left and right):
        #Sol listedeki elemanlar bitene dek sağ liste elemanlaro ile birer birer kıyaslanır.
        if left[0] < right[0]:
            #Sol sağdan küçükse resulta eklenir ve pop edilir.
            result.append(left[0])
            left.pop(0)
        else:
            #Sağ küçükse aynı işlem sağ için gerçekleştirilir.
            result.append(right[0])
            right.pop(0)
       #Herhangi bir listede eleman bittiyse geriye kalanlar aşağıdaki şekilde listelere aynen eklenir.
    if left:
        result += left
    if right:
        result += right

    return result


liste1 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202,
          534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]

print('Sıralama öncesi: ', liste1)
print('Sıralama sonrası: ', merge_sort(liste1))
