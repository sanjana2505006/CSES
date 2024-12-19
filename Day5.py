def beautiful_permutation(n):
    if n == 1:
        print(1)
    elif n == 2:
        print(2, 1)
    elif n == 3:
        print("NO SOLUTION")
    else:
        even = [i for i in range(2, n + 1, 2)]  
        odd = [i for i in range(1, n + 1, 2)]   
        print(*even, *odd)  
n = int(input())
beautiful_permutation(n)
