def search_pairs(array: list, k: int):
    s = set()
    for i in array:
        if(k-i in array):
            a=[i,k-i]
            a.sort()
            s.add(tuple(a))
    print(list(s))

# проверка
search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5)
