def min_moves_to_increasing_array(n, arr):
    moves = 0
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            moves += arr[i-1] - arr[i]
            arr[i] = arr[i-1]
    return moves
n = int(input())
arr = list(map(int, input().split()))
print(min_moves_to_increasing_array(n, arr))