def selection_sort(L):
    n = len(L)
    sorted_L = []
    for i in range(n):
        minimum = min(L)
        L.remove(minimum)
        sorted_L.append(minimum)

    return sorted_L


L = [1, 4, 5, 2, 3]
result = selection_sort(L)
print(result)