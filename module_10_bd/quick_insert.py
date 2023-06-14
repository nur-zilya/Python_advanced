A = [1,2,3,3,3,5]
x = 4


def quick_insert(row, num):
    low = 0
    high = len(row) - 1

    while low <= high:
        mid = (low + high)//2

        if row[mid] == num:
            return row[mid]
        elif row[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    print (low)


if __name__ == "__main__":
    quick_insert(A, x)
