def find_rotation_point(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[right]:
            # Средний элемент больше правого элемента, сдвиг находится в правой половине
            left = mid + 1
        else:
            # Средний элемент меньше или равен правому элементу, сдвиг находится в левой половине
            right = mid

    return left

# Примеры
arr1 = [1, 2, 3, 5, -8, -6, -1, 0]
arr2 = [2, 3, 4, 5, 0, 1]

rotation_point1 = find_rotation_point(arr1)
rotation_point2 = find_rotation_point(arr2)

print("Сдвиг для массива 1:", rotation_point1)
print("Сдвиг для массива 2:", rotation_point2)
