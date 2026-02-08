arr = [1, 2, 3, 4, 5, 6, 7, 8]  # sorted arr ?? , fibonacci search --> sorted
target = 7


def Binary(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    taregt_idx = Binary(arr, target)
    print(taregt_idx)
