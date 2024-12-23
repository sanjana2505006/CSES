def number_spiral(t, queries):
    results = []
    for y, x in queries:
        n = max(y, x)
        if n % 2 == 0: 
            if y == n:
                results.append(n**2 - (x - 1))
            else:
                results.append((n - 1)**2 + y)
        else:  
            if x == n:
                results.append(n**2 - (y - 1))
            else:
                results.append((n - 1)**2 + x)
    return results
t = int(input())
queries = [tuple(map(int, input().split())) for _ in range(t)]
answers = number_spiral(t, queries)
print('\n'.join(map(str, answers)))