def rotate_list(items, k):
    k = k % len(items)
    return items[k:] + items[:k]
