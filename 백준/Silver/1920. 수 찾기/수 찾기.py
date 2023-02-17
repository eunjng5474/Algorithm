def search(arr, check):
    start = 0
    end = len(arr) - 1

    while start <= end:
        middle = (start + end) // 2
        if check == arr[middle]:
            return 1
        elif check < arr[middle]:
            end = middle - 1
        elif check > arr[middle]:
            start = middle + 1
    return 0


N = int(input())
ai = list(map(int, input().split()))
arr = sorted(ai)

M = int(input())
check = list(map(int, input().split()))

for c in check:
    print(search(arr, c))
